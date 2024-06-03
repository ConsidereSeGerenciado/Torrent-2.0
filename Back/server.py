import socket
import os
import threading

PORT = 5000
UPLOADS_DIR = "uploads"

def handle_client(client_socket, address):
    print(f"[CONEXÃO] Recebido novo cliente de {address}")

    command = client_socket.recv(1024).decode('utf-8')

    if command == "DOWNLOAD":
        # Cliente solicitou download
        filename = client_socket.recv(1024).decode('utf-8')
        print(f"[RECEBENDO] Solicitação de download: {filename}")

        if not os.path.exists(os.path.join(UPLOADS_DIR, filename)):
            print(f"[ERRO] Arquivo não encontrado: {filename}")
            client_socket.send(f"Arquivo não encontrado".encode('utf-8'))
            return

        with open(os.path.join(UPLOADS_DIR, filename), 'rb') as file:
            file_data = file.read(1024)
            while file_data:
                client_socket.send(file_data)
                file_data = file.read(1024)

        print(f"[ENVIADO] Arquivo {filename} enviado para {address}")

    elif command == "UPLOAD":
        # Cliente deseja enviar um arquivo
        filename = client_socket.recv(1024).decode('utf-8')
        print(f"[RECEBENDO] Arquivo para upload: {filename}")

        save_path = os.path.join(UPLOADS_DIR, filename)
        with open(save_path, 'wb') as file:
            file_data = client_socket.recv(1024)
            while file_data:
                file.write(file_data)
                file_data = client_socket.recv(1024)

        print(f"[SALVO] Arquivo {filename} salvo em {save_path}")
        client_socket.send(b"Arquivo recebido com sucesso!".encode('utf-8'))

    else:
        print(f"[ERRO] Comando inválido: {command}")
        client_socket.send(f"Comando inválido".encode('utf-8'))
        client_socket.close()
        return

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', PORT))
server_socket.listen(5)

print(f"[SERVIDOR] Ouvindo em localhost:{PORT}")

while True:
    client_socket, address = server_socket.accept()
    threading.Thread(target=handle_client, args=(client_socket, address)).start()
