import socket
import os
import threading

PORT = 5000
RECEBIDOS_DIR = "uploads"

def handle_client(client_socket, address):
    print(f"[CONEXÃO] Recebido novo cliente de {address}")

    
    filename = client_socket.recv(1024).decode('utf-8')
    print(f"[RECEBENDO] Arquivo: {filename}")

    
    if not os.path.exists(os.path.join(RECEBIDOS_DIR, filename)):
        print(f"[ERRO] Arquivo não encontrado: {filename}")
        client_socket.send(f"Arquivo não encontrado".encode('utf-8'))
        return

    
    with open(os.path.join(RECEBIDOS_DIR, filename), 'rb') as file:
        file_data = file.read(1024)
        while file_data:
            client_socket.send(file_data)
            file_data = file.read(1024)

    print(f"[ENVIADO] Arquivo {filename} enviado para {address}")
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', PORT))
server_socket.listen(5)

print(f"[SERVIDOR] Ouvindo em localhost:{PORT}")
while True:
    client_socket, address = server_socket.accept()
    threading.Thread(target=handle_client, args=(client_socket, address)).start()
