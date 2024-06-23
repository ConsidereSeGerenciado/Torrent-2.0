import libtorrent as lt
import time

def configure_libtorrent_session():
    session = lt.session()
    session.listen_on(6881, 6891)  # Defina o intervalo de portas para a sessão
    
    # Outras configurações opcionais
    session.start_dht()
    session.start_upnp()
    session.start_lsd()

    # Mantenha a sessão ativa
    while True:
        time.sleep(1)

if __name__ == "__main__":
    configure_libtorrent_session()
