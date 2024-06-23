import sys
import webbrowser
import os
import json
from pathlib import Path
from unidecode import unidecode

import requests
import bencodepy
import hashlib
from torrentool.api import Torrent
import time
import threading
import base64
import urllib.parse
import subprocess

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea,QFileDialog,QSpacerItem, QDialogButtonBox, QDialog
)
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import Qt, Signal, QTimer

from Header import header
from Menu import menu
from Home import initUI
from tipo import initUI1
from biblioteca import initUI2
from config import initUI3
from genero import initUI4
from titulo import initUI5
from upload import initUI6

CONFIG_FILE = '../Back/config.json'
    
class ClickableImageLabel(QLabel):
    clicked = Signal()

    def __init__(self, pixmap, width, height, parent=None):
        super().__init__(parent)
        self.setPixmap(pixmap.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.setFixedSize(width, height)
        
    def mousePressEvent(self, event):
        self.clicked.emit()


torrents_info = []
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
       

    def initUI(self):
        self.setWindowTitle("PyTorrent")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.get_all_torrents_info()

        self.content_header = header(self)
        self.content_menu = menu(self)
        self.content_pesquisa_layout = initUI(self)

        self.content_menu.addLayout(self.content_pesquisa_layout)
        self.content_header.addLayout(self.content_menu)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.content_header)
        self.setCentralWidget(self.central_widget)
        pass

    def menos_clicked(self):
        print("menos clicked")
        self.showMinimized()

    def quadrado_clicked(self):
        print("quadrado clicked")
        if self.isFullScreen():
            self.showNormal()  # Se já estiver em fullscreen, voltar ao tamanho normal
        else:
            self.showFullScreen()  # Caso contrário, ativar o fullscreen

    def fechar_clicked(self):
        print("fecha clicked")
        self.close()

    def home_clicked(self):
        global i
        i= 0
        print("Home clicked")
        self.update_interface()

    def tipo_clicked(self):
        global i
        i = 1
        print("Tipo clicked")
        self.update_interface()

    def biblioteca_clicked(self):
        global i
        i = 2
        print("Biblioteca clicked")
        self.update_interface()

    def upload_clicked(self):
        global i 
        i = 6
        print("Upload clicked")
        self.update_interface()

    def config_clicked(self):
        global i
        i = 3
        print("Config clicked")
        self.update_interface()

    def github_clicked(self):
        url = 'https://github.com/gabrielmaiaaa/Torrent-2.0'
        webbrowser.open_new_tab(url)  
        print("Github clicked")

    def genero_clicked(self,name):
        global i
        i = 4
        print("Genero clicked")
        self.update_interface(name)
    
    def titulo_clicked(self, name,tipo):
        global i 
        i = 5
        print("titulo clicked")
        self.update_interface(name,tipo)

    def update_interface(self,name=None,tipo=None):
        global i
        # Limpar o layout do content_pesquisa_layout
        while self.content_pesquisa_layout.count():
            item = self.content_pesquisa_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        if i == 1:
            new_layout = initUI1(self)
        elif i == 0:
            new_layout = initUI(self)
        elif i == 2:
            new_layout = initUI2(self)
        elif i == 3:
            new_layout = initUI3(self)
        elif i == 4:
            new_layout = initUI4(self,name)
        elif i == 5:
            new_layout = initUI5(self,name,tipo)
        elif i == 6:
            new_layout = initUI6(self)

        self.content_pesquisa_layout.addLayout(new_layout)

    def on_enter(self, button):
        button.setStyleSheet("""
            background-color: gray;
            border: none;
            padding: 0px;
        """)

    def on_leave(self, button):
        button.setStyleSheet("""
            background-color: black;
            border: none;
            padding: 0px;
        """)

    def check_fields(self):
        nome_filled = bool(self.nome_widget1.text().strip())
        arquivo_filled = bool(self.directory_edit_arquivo.text().strip())
        midia_selected = self.midia_widget1.currentIndex() != 0

        if nome_filled and arquivo_filled and midia_selected:
            self.button_widget.setEnabled(True)
            self.button_widget.setStyleSheet("border: 2px solid white; padding: 0px; background-color: black")
        else:
            self.button_widget.setEnabled(False)

    def on_upload_click(self):
        # Assim q clica no botão, eu mudo a cor para uma nova para simular o efeito de um click
        self.button_widget.setStyleSheet("border: 2px solid white; padding: 0px; background-color: lightgray")
        # Temporizador para ele voltar para o fundo de cor original
        QTimer.singleShot(200, lambda: self.button_widget.setStyleSheet("border: 2px solid white; padding: 0px; background-color: black"))
        self.collect_and_upload()
        self.start_progress()
        


    def start_progress(self):
        self.progress_value = 0
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(self.progress_value)
        self.timer.start(100)      

    def start_progress1(self):
        print('teste ' + self.link_magnetico)
        self.start_download(self.link_magnetico)
        self.progress_value = 0
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(self.progress_value)
        self.timer.start(100)  # Define o intervalo de atualização em milissegundos

    def update_progress(self):
        self.progress_value += 1
        self.progress_bar.setValue(self.progress_value)
        if self.progress_value >= 100:
            self.timer.stop()

    def create_torrent(self, input_path, output_dir, tracker_url, name=None, type=None, description=None):
        torrent_data = {
            'announce': tracker_url,
            'info': {
                'piece length': 256 * 1024  # 256 KB por pedaço (piece)
            }
        }

        if os.path.isfile(input_path):
            # Se for um arquivo único
            torrent_data['info']['name'] = os.path.basename(input_path)
            torrent_data['info']['length'] = os.path.getsize(input_path)
            torrent_data['info']['pieces'] = self.calculate_pieces(input_path, torrent_data['info']['piece length'])
        elif os.path.isdir(input_path):
            # Se for uma pasta
            torrent_data['info']['name'] = os.path.basename(input_path)
            torrent_data['info']['files'] = []
            torrent_data['info']['pieces'] = b''

            # Calcular hash SHA-1 de cada pedaço de arquivo na pasta
            for root, _, files in os.walk(input_path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    relative_path = os.path.relpath(file_path, input_path)
                    file_size = os.path.getsize(file_path)

                    torrent_data['info']['files'].append({
                        'length': file_size,
                        'path': relative_path.split(os.path.sep)
                    })
                    torrent_data['info']['pieces'] += self.calculate_pieces(file_path, torrent_data['info']['piece length'])
        else:
            raise ValueError("O caminho especificado não é válido.")

        # Adicionar nome, tipo e descrição ao torrent_data
        if name:
            torrent_data['info']['name'] = name
        if type:
            torrent_data['info']['type'] = type
        if description:
            torrent_data['info']['description'] = description

        # Diretório de saída para salvar o arquivo .torrent
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            torrent_file_path = os.path.join(output_dir, f'{os.path.basename(input_path)}.torrent')
        else:
            torrent_file_path = f'{os.path.basename(input_path)}.torrent'

        # Salvando o arquivo torrent
        with open(torrent_file_path, 'wb') as f:
            f.write(bencodepy.encode(torrent_data))

        return torrent_file_path

    def calculate_pieces(self, file_path, piece_length):
        pieces = b''
        with open(file_path, 'rb') as f:
            while True:
                piece = f.read(piece_length)
                if not piece:
                    break
                pieces += hashlib.sha1(piece).digest()
        return pieces

    def create_magnet_link(self, torrent_file):
        # Leitura do arquivo torrent
        with open(torrent_file, 'rb') as f:
            torrent_data = f.read()

        # Decodificação do arquivo torrent
        metadata = bencodepy.decode(torrent_data)

        # Calculando o hash SHA-1 do info_hash
        info_hash = hashlib.sha1(bencodepy.encode(metadata[b'info'])).digest()

        # Codificando o hash SHA-1 em Base32
        base32_info_hash = base64.b32encode(info_hash).decode().strip('=')

        # Construindo o link magnético
        magnet_link = f'magnet:?xt=urn:btih:{base32_info_hash}'

        # Adicionando o tracker URL ao link magnético, se disponível
        if b'announce' in metadata:
            tracker_url = urllib.parse.quote(metadata[b'announce'].decode())
            magnet_link += f'&tr={tracker_url}'
        
        return magnet_link

    def collect_and_upload(self):
        downloads_path = self.load_download_path()  # Função para carregar o caminho de downloads
        diretorio_arquivo = self.directory_edit_arquivo.text()  # Supondo que esses métodos são do PyQt ou similar
        nome = self.nome_widget1.text()
        tipo_midia = self.midia_widget1.currentText()
        descricao = self.descricao_widget1.toPlainText()

        if not descricao:
            descricao = "Sem descrição"

        # Criar o arquivo torrent
        torrent_file = self.create_torrent(str(diretorio_arquivo), downloads_path, 'http://18.191.81.105:6969/tracker',
                                           name=nome, type=tipo_midia, description=descricao)
        # Gerar e imprimir o link magnético
        magnet_link = self.create_magnet_link(torrent_file)
        
        print("Link Magnético:", magnet_link)
        self.start_seed(magnet_link)
        self.upload_infos(nome,tipo_midia,descricao,magnet_link)
    
    def upload_infos(self, nome, tipo_midia,descricao,magnet_link):

        params = {
            'nome': nome,
            'tipo_midia': tipo_midia,
            'descricao': descricao,
            'link_magnetico': magnet_link
        }

        try:
            response = requests.get('http://18.191.81.105:6969/dados', params=params)
            if response.status_code == 200:
                print("Sucesso", "Dados enviados com sucesso!")
            else:
                print("Erro", f"Falha ao enviar dados: {response.text}")
        except Exception as e:
            print("Erro", f"Ocorreu um erro: {e}")


    def start_download(self, magnet_link):
        save_path = self.load_download_path()  # Supondo que load_download_path retorna o diretório correto
        command = [
            'aria2c', 
            '--seed-time=0', 
            '--enable-dht', 
            '--dht-listen-port=6881', 
            '--listen-port=6881',
            '--dir=' + str(save_path), 
            magnet_link
        ]
        subprocess.run(command)
    
    def start_seed(self, torrent_file):
        print(torrent_file)
        save_path = self.load_download_path()  # Supondo que load_download_path retorna o diretório correto
        # Comando para iniciar o seeding com aria2c
        command = [
            'aria2c', 
            '--seed-time=0', 
            '--enable-dht',
            '--dht-listen-port=6881', 
            '--listen-port=6881',
            '--dir=' + str(save_path), 
            torrent_file
        ]
        subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Started seeding {torrent_file}")

    
    def get_all_torrents_info(self):
        tracker_url = 'http://18.191.81.105:6969/dados/torrents'
        global torrents_info
        
        try:
            response = requests.get(tracker_url)
            response.raise_for_status()  # Raise exception for 4xx or 5xx errors
            decoded_data = bencodepy.decode(response.content)

            torrents_info = [
            {
                key.decode(): value.decode() if isinstance(value, bytes) else value
                for key, value in item.items()
            }
            for item in decoded_data
            ]

            return  torrents_info

        except requests.exceptions.RequestException as e:
            print(f"Error fetching torrents info: {e}")
        
        return b''  # Retorna uma string vazia codificada em Bencode se algo der errado
    
    def ListaAtualizada(self):
        global torrents_info
        return torrents_info
    

    def openFileDialog(self):
       # Criação do diálogo para seleção de arquivos
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        
        # Adiciona botão para selecionar pasta
        button_box = dialog.findChild(QDialogButtonBox)
        select_folder_button = QPushButton("Selecionar Pasta", dialog)
        button_box.addButton(select_folder_button, QDialogButtonBox.ActionRole)
        
        # Conecta o botão para abrir o diálogo de seleção de pasta
        select_folder_button.clicked.connect(lambda: self.selectFolder(dialog))

        if dialog.exec():
            selected_files = dialog.selectedFiles()
            if selected_files:
                self.directory_edit_arquivo.setText(selected_files[0])
    
    def selectFolder(self, dialog):
        folder_path = QFileDialog.getExistingDirectory(None, "Selecionar Pasta", "")
        if folder_path:
            self.directory_edit_arquivo.setText(folder_path)
            dialog.reject()  # Fecha o diálogo de arquivo


    def OpenFileA(self):
        folder = QFileDialog.getExistingDirectory(self, 'Selecionar Pasta', str(Path.home()))
        if folder:
            downloads_path = Path(folder)
            self.line_download.setText(str(downloads_path))

    def populate_layout(self, items):

        sorted_items = sorted(items, key=lambda x: x[0])
        self.content_layout1.setAlignment(Qt.AlignTop)

        for row, (text, image_path) in enumerate(sorted_items):    
            button1 = ClickableImageLabel(QPixmap(image_path), 270, 90)
            button1.clicked.connect(lambda text=text: self.genero_clicked(text))
            button1.setStyleSheet("border:2px solid white; padding: 0px;")
            
            label = QLabel(text)
            label.setFont(QFont("Abril FatFace", 20, QFont.Bold))
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("border: none; padding: 0px; background-color: transparent")
            
            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)  
            layout.setSpacing(0)  
            layout.addWidget(label, alignment=Qt.AlignCenter)
            button1.setLayout(layout)

            self.content_layout1.addWidget(button1, row // 2, row % 2)

    def home_layout(self, items):

        sorted_items = sorted(items, key=lambda x: x['nome'])  
        self.content_layout1.setAlignment(Qt.AlignTop)

        for idx, item  in enumerate(sorted_items):
            name = item['nome']
            tipo = item['tipo_midia']
            description = item['descricao']
            button1 = ClickableImageLabel(QPixmap('Imagens/cinza.png'), 270, 90)
            button1.clicked.connect(lambda name=name, tipo=tipo: self.titulo_clicked(name,tipo))
            button1.setStyleSheet("border:2px solid white; padding: 0px;")
            
            label_tipo = QLabel(tipo)
            label_tipo.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            label_tipo.setStyleSheet("border: 1px solid white; padding: 0px 1px 0px 1px; background-color: black; border-radius: 10px;")
            label_tipo.setFixedSize(label_tipo.sizeHint())
            
            label_nome = QLabel(name)  
            label_nome.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
            label_nome.setStyleSheet("color: white; border: 1px solid white; padding: 0px 4px 0px 4px; background-color: black; border-radius: 10px;")
            label_nome.setFixedSize(label_nome.sizeHint())

            button1.setLayout(QVBoxLayout())
            button1.layout().addWidget(label_tipo, alignment=Qt.AlignTop) 
            
            button1.layout().addWidget(label_nome, alignment=Qt.AlignHCenter)
            
            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)  
            layout.setSpacing(0)  
            layout.addWidget(button1)  
            self.content_layout1.addLayout(layout, idx // 2, idx % 2)
        

    def filtrar_conteudo(self):
        texto_busca = unidecode(self.line_edit_busca.text().lower())
        for i in reversed(range(self.content_layout1.count())):
            self.content_layout1.itemAt(i).widget().setParent(None)

        if texto_busca == "":
            filtered_items = self.items
        else:
            filtered_items = [item for item in self.items if texto_busca in item[0].lower()]
        
        self.populate_layout(filtered_items)

    def filtrar_conteudo1(self):
        texto_busca = unidecode(self.line_edit_busca.text().lower())

        while self.content_layout1.count():
            child = self.content_layout1.takeAt(0)
            if child.layout():
                while child.layout().count():
                    grandchild = child.layout().takeAt(0)
                    if grandchild.widget():
                        grandchild.widget().deleteLater()
                child.layout().deleteLater()
            elif child.widget():
                child.widget().deleteLater()

        if texto_busca == "":
            filtered_items = self.data_list
            self.destaques_widget.setVisible(True)
            self.destaque_widget.setVisible(True)
            self.populares_widget.setVisible(True)
        else:
            filtered_items = [item for item in self.data_list if texto_busca in item[0].lower()]   
            self.destaques_widget.setVisible(False)
            self.destaque_widget.setVisible(False)
            self.populares_widget.setVisible(False)

        self.home_layout(filtered_items)

    
    def descricaoSearch(self, name,tipo):
        data_list = self.ListaAtualizada()
        for item in data_list:
            if item['nome'] == name and item['tipo_midia'] == tipo:
                return item['descricao']
    
    def linkSearch(self, name, tipo):
        data_list = self.ListaAtualizada()
        for item in data_list:
            if item['nome'] == name and item['tipo_midia'] == tipo:
                return item['link_magnetico']
        
    
    def load_download_path(self):
        config_path = Path(CONFIG_FILE)
        if not config_path.exists():
            default_path = Path.home() / 'Downloads'
            self.save_download_path(default_path)
            return default_path

        with config_path.open('r') as f:
            config = json.load(f)
            downloads_path = Path(config.get('downloads_path', str(Path.home() / 'Downloads')))
            return downloads_path
    
    def save_download_path(self, path):
        with open(CONFIG_FILE, 'w') as f:
            json.dump({'downloads_path': str(path)}, f) 
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
    # Aceita conexões vindas de clientes
