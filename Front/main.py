import sys
import webbrowser
from unidecode import unidecode

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea,QFileDialog
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

    def genero_clicked(self):
        global i
        i = 4
        print("Genero clicked")
        self.update_interface()
    
    def titulo_clicked(self):
        global i 
        i = 5
        print("titulo clicked")
        self.update_interface()

    def update_interface(self):
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
            new_layout = initUI4(self)
        elif i == 5:
            new_layout = initUI5(self)
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

    def openFileDialog(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Selecionar Arquivo")
        if file_path:
            self.directory_edit_arquivo.setText(file_path)
    
    def openFileDialog1(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Selecionar Arquivo")
        if file_path:
            self.directory_edit_imagem.setText(file_path)

    def OpenFileA(self):
        directory = QFileDialog.getExistingDirectory(self, "Selecione uma pasta", "/")
        if directory:
            self.line_download.setText(directory)

    def populate_layout(self, items):

        self.content_layout1.setAlignment(Qt.AlignTop)

        for row, (text, image_path) in enumerate(items):
            
            button1 = ClickableImageLabel(QPixmap(image_path), 270, 90)
            button1.clicked.connect(self.genero_clicked)
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

    def filtrar_conteudo(self):
        texto_busca = unidecode(self.line_edit_busca.text().lower())
        for i in reversed(range(self.content_layout1.count())):
            self.content_layout1.itemAt(i).widget().setParent(None)

        if texto_busca == "":
            filtered_items = self.items
        else:
            filtered_items = [item for item in self.items if texto_busca in item[0].lower()]
        
        self.populate_layout(filtered_items)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
