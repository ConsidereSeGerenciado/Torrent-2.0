import sys
import webbrowser
import os
import json
from pathlib import Path
from unidecode import unidecode

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea,QFileDialog,QSpacerItem,
)
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import Qt, Signal

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyTorrent")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.content_header = header(self)
        self.content_menu = menu(self)
        self.content_pesquisa_layout = initUI(self)

        self.content_menu.addLayout(self.content_pesquisa_layout)
        self.content_header.addLayout(self.content_menu)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.content_header)
        self.setCentralWidget(self.central_widget)

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
        self.collect_and_upload()
        self.start_progress()

    def start_progress(self):
        self.progress_value = 0
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(self.progress_value)
        self.timer.start(100)  # Define o intervalo de atualização em milissegundos

    def update_progress(self):
        self.progress_value += 1
        self.progress_bar.setValue(self.progress_value)
        if self.progress_value >= 100:
            self.timer.stop()

    def collect_and_upload(self):
        nome = self.nome_widget1.text()
        diretorio_arquivo = self.directory_edit_arquivo.text()
        tipo_midia = self.midia_widget1.currentText()
        descricao = self.descricao_widget1.toPlainText()
        diretorio_imagem = self.directory_edit_imagem.text()
        
        self.upload_arquivos(nome, diretorio_arquivo, tipo_midia, descricao, diretorio_imagem)

    def upload_arquivos(self, nome, diretorio_arquivo, tipo_midia, descricao, diretorio_imagem):
        # Se a descrição estiver vazia, define como "Sem descrição"
        if not descricao:
            descricao = "Sem descrição"
        # Se o diretório da imagem estiver vazio, define como "../Back/Imagens/Sem_Imagem.png"
        if not diretorio_imagem:
            diretorio_imagem = "../Back/Imagens/Sem_Imagem.png"
        
        # Formata a linha a ser adicionada ao arquivo de dados
        linha = f"{nome}, {tipo_midia}, {diretorio_imagem}, {descricao}\n"
        print(linha)
        # Caminho dcd o arquivo de dados
        file_path = '../Back/Dados.txt'

        # Adiciona a linha ao arquivo de dados
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(linha)


    def openFileDialog(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Selecionar Arquivo")
        if file_path:
            self.directory_edit_arquivo.setText(file_path)
    
    def openFileDialog1(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Selecionar Arquivo")
        if file_path:
            self.directory_edit_imagem.setText(file_path)

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

        sorted_items = sorted(items, key=lambda x: x[0])
        self.content_layout1.setAlignment(Qt.AlignTop)

        for row, (name, tipo, image_path, description) in enumerate(sorted_items):
            button1 = ClickableImageLabel(QPixmap(image_path), 270, 90)
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
            self.content_layout1.addLayout(layout, row // 2, row % 2)
        

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

    def imageSearch(self, name,tipo):
        file_path = '../Back/Dados.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                elements = line.split(', ', 3)
                if elements[0] == name:
                    if elements[1] == tipo:
                        return elements[2]  # Retorna o caminho da imagem
        return None  # Retorna None se o nome não for encontrado

    def descricaoSearch(self, name,tipo):
        file_path = '../Back/Dados.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                elements = line.split(', ', 3)
                if elements[0] == name:
                    if elements[1] == tipo:
                        return elements[3]  # Retorna a descrição
        return None  # Retorna None se o nome não for encontrado
    
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
