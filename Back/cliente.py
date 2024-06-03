import socket

def send_file(filename, server_address, server_port):
    # Cria o socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conecta o socket ao servidor
        client_socket.connect((server_address, server_port))

        # Envia o nome do arquivo
        client_socket.send(filename.encode())

        # Abre o arquivo para leitura binária
        with open(filename, 'rb') as f:
            # Envia os dados do arquivo para o servidor
            data = f.read(1024)
            while data:
                client_socket.send(data)
                data = f.read(1024)

    except Exception as e:
        print(f"Erro ao enviar arquivo: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_address = 'localhost'  # Endereço IP do servidor
    server_port = 5000  # Porta do servidor
    filename = "/home/martins/Downloads/avl.c"  # Caminho do arquivo a ser enviado

    send_file(filename, server_address, server_port)
