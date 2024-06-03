import socket
import os

HOST = "localhost"  # Endereço do servidor
PORT = 5000  # Porta do servidor

def main():
    # Conectar ao servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        # Receber o comando do usuário
        command = input("Digite DOWNLOAD para baixar ou UPLOAD para enviar um arquivo: ").upper()
        client_socket.send(command.encode('utf-8'))

        if command == "DOWNLOAD":
            filename = input("Digite o nome do arquivo para baixar: ")
            client_socket.send(filename.encode('utf-8'))

            # Receber o arquivo do servidor e salvá-lo localmente
            with open(filename, 'wb') as file:
                file_data = client_socket.recv(1024)
                while file_data:
                    file.write(file_data)
                    file_data = client_socket.recv(1024)
            print(f"Arquivo {filename} baixado com sucesso!")

        elif command == "UPLOAD":
            filename = input("Digite o nome do arquivo para enviar: ")
            if not os.path.exists(filename):
                print(f"Erro: Arquivo {filename} não encontrado.")
                return

            # Enviar o arquivo para o servidor
            with open(filename, 'rb') as file:
                file_data = file.read(1024)
                while file_data:
                    client_socket.send(file_data)
                    file_data = file.read(1024)
            print(f"Arquivo {filename} enviado com sucesso!")

        else:
            print("Comando inválido.")

if __name__ == "__main__":
    main()
