import socket
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enviar_arquivo(host_servidor, porta_servidor, caminho_arquivo, buffer_size=4096):
    try:
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect((host_servidor, porta_servidor))
        logging.info(f'Conectado ao servidor {host_servidor}:{porta_servidor}')
        
        
        nome_arquivo = os.path.basename(caminho_arquivo)
        cliente_socket.send(nome_arquivo.encode())
        
        
        with open(caminho_arquivo, 'rb') as arquivo:
            while True:
                bytes_lidos = arquivo.read(buffer_size)
                if not bytes_lidos:
                    break
                cliente_socket.sendall(bytes_lidos)
        
        logging.info(f'{nome_arquivo} enviado com sucesso para {host_servidor}:{porta_servidor}')
    except Exception as e:
        logging.error(f'Erro ao enviar arquivo: {e}')
    finally:
        cliente_socket.close()
        logging.info('Conexão com o servidor encerrada')

if __name__ == "__main__":
    host_servidor = '127.0.0.1'  # Endereço do "servidor"
    porta_servidor = 5001        # Porta do servidor
    caminho_arquivo = 'caminho/para/seu/arquivo.txt'  # Caminho para o arquivo a ser enviado
    
    enviar_arquivo(host_servidor, porta_servidor, caminho_arquivo)
