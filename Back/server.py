import socket
import os
import threading
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_client_connection(conn, addr, buffer_size=4096):
    logging.info(f'Conexão estabelecida com {addr}')
    
    try:
        
        nome_arquivo = conn.recv(buffer_size).decode()
        if not nome_arquivo:
            raise ValueError("Nome do arquivo não recebido.")
        
        caminho_arquivo = os.path.join('uploads', nome_arquivo)
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        
        
        with open(caminho_arquivo, 'wb') as arquivo:
            while True:
                bytes_lidos = conn.recv(buffer_size)
                if not bytes_lidos:
                    break
                arquivo.write(bytes_lidos)
        
        logging.info(f'Arquivo {nome_arquivo} recebido com sucesso de {addr}')
        
        
        conn.send(b'Arquivo recebido com sucesso!')
    except Exception as e:
        logging.error(f'Erro ao receber arquivo de {addr}: {e}')
    finally:
        conn.close()
        logging.info(f'Conexão com {addr} encerrada')

def iniciar_servidor(host='0.0.0.0', port=5001, buffer_size=4096):
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, port))
    servidor_socket.listen(5)
    logging.info(f'Servidor escutando em {host}:{port}')
    
    try:
        while True:
            conn, addr = servidor_socket.accept()
            cliente_thread = threading.Thread(target=handle_client_connection, args=(conn, addr, buffer_size))
            cliente_thread.start()
    except KeyboardInterrupt:
        logging.info('Servidor interrompido manualmente')
    except Exception as e:
        logging.error(f'Erro no servidor: {e}')
    finally:
        servidor_socket.close()
        logging.info('Servidor encerrado')

if __name__ == "__main__":
    iniciar_servidor()
