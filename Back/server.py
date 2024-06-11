import os
import time
import signal
import socket
import hashlib
import bencoding

from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


DOWNLOAD_DIR = "/upload"
PORT = 8080
TIMEOUT = 300  # Segundos

def load_torrent(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return bencoding.decode(data)

def get_info_hash(torrent):
    info = torrent["info"]
    return hashlib.sha1(bencoding.encode(info)).hexdigest()

def get_piece_hashes(torrent):
    info = torrent["info"]
    pieces = info["pieces"]
    piece_hashes = []
    for i in range(0, len(pieces), 20):
        piece_hashes.append(pieces[i:i + 20])
    return piece_hashes

class PeerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        peer_info = parse_qs(urlparse(self.path).query)
        peer_id = peer_info["peer_id"][0].decode("hex")
        ip = self.client_address[0]
        port = int(peer_info["port"][0])
        self.server.peers[peer_id] = Peer(ip, port)

class TrackerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        params = parse_qs(urlparse(self.path).query)
        peer_id = params["peer_id"][0].decode("hex")
        ip = self.client_address[0]
        port = int(params["port"][0])
        downloaded = int(params["downloaded"][0])
        uploaded = int(params["uploaded"][0])

        self.server.tracker.update_peer(peer_id, ip, port, downloaded, uploaded)

class Tracker:
    def __init__(self, torrent_info_hash):
        self.torrent_info_hash = torrent_info_hash
        self.peers = {}

    def update_peer(self, peer_id, ip, port, downloaded, uploaded):
        if peer_id not in self.peers:
            self.peers[peer_id] = Peer(ip, port)
        self.peers[peer_id].update(downloaded, uploaded)

    def get_peers(self):
        return list(self.peers.values())

class PieceManager:
    def __init__(self, torrent_info):
        self.piece_hashes = get_piece_hashes(torrent_info)
        self.available_pieces = set()
        self.downloaded_pieces = set()

    def add_piece(self, piece_hash):
        self.available_pieces.add(piece_hash)

    def mark_piece_downloaded(self, piece_hash):
        self.available_pieces.remove(piece_hash)
        self.downloaded_pieces.add(piece_hash)

    def get_available_pieces(self):
        return list(self.available_pieces)

    def is_complete(self):
        return len(self.downloaded_pieces) == len(self.piece_hashes)

class Server:
    def __init__(self, torrent_filename):
        self.torrent = load_torrent(torrent_filename)
        self.info_hash = get_info_hash(self.torrent)
        self.piece_manager = PieceManager(self.torrent["info"])
        self.tracker = Tracker(self.info_hash)
        self.peers = {}

        self.start_tracker()
        self.start_http_server()

    def start_tracker(self):
        tracker_thread = Thread(target=self.tracker.run, daemon=True)
        tracker_thread.start()

    def start_http_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("0.0.0.0", PORT))
            s.listen(5)

            while True:
                conn, addr = s.accept()
                with conn:
                    if addr[0] == "127.0.0.1":  # Conexão local
                        handler = PeerHandler(conn, self)
                    else:
                        handler = TrackerHandler(conn, self)
                    handler.serve_forever()

    def download_piece_from_peer(self, peer):
        piece_hash = self.piece_manager.get_available_pieces()[0]
        piece_data = peer.download_piece(piece_hash)
        if piece_data:
            self.piece_manager.add_piece(piece_hash)
            self.save_piece(piece_hash, piece_data)
            self.piece_manager.mark_piece_downloaded(piece_hash)

    def save_piece(self, piece_hash, piece_data):
        filename = os.path.join(DOWNLOAD_DIR, self.torrent["info"]["name"] + ".torrent")
        with open(filename, "rb") as f:
            torrent_data = f.read()

        piece_index = self.piece_manager.piece_hashes.index(piece_hash)
        offset = piece_index * self.torrent["info"]["piece length"]
        new_data = torrent_data[:offset] + piece_data + torrent_data[offset + len(piece_data):]

        with open(filename, "wb") as f:
            f.write(new_data)

    def download_torrent(self):
        while not self.piece_manager.is_complete():
            available_peers = self.tracker.get_peers()
            for peer in available_peers:
                if peer.has_piece(self.piece_manager.get_available_pieces()[0]):
                    self.download_piece_from_peer(peer)
                    break

            time.sleep(1)

        print("Download concluído!")

if __name__ == "__main__":
    torrent_filename = "arquivo.torrent"  # MANO, TESTA COM ARQUIVO .TORRENT
    server = Server(torrent_filename)
    server.download_torrent()
