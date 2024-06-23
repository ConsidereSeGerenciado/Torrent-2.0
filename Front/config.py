from pathlib import Path

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea, QFrame, QGridLayout
)
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import Qt, Signal

class ClickableImageLabel(QLabel):
    clicked = Signal()

    def __init__(self, pixmap, width, height):
        super().__init__()
        self.setPixmap(pixmap.scaled(width, height))
        self.setFixedSize(width, height)
        self.setAlignment(Qt.AlignCenter)
        self.setScaledContents(True)
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        self.clicked.emit()

def initUI3(self):
   
    # Área da pesquisa
    content_pesquisa_layout = QVBoxLayout() 

    pesquisa_widget = QWidget()
    pesquisa_widget.setStyleSheet("background-color: #242121; border-bottom: 2px solid white;")
    pesquisa_widget.setFixedHeight(80)
    pesquisa_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    pesquisa_layout = QHBoxLayout(pesquisa_widget)

    label_seta = ClickableImageLabel(QPixmap("Imagens/voltar.png"),512,512)
    label_seta.setStyleSheet("border:none; padding: 0px;")
    label_seta.clicked.connect(self.home_clicked)
    label_seta.setStyleSheet("border-bottom: none; padding: 0px;")
    label_seta.setFixedSize(50,30)
    pesquisa_layout.addWidget(label_seta, alignment=Qt.AlignCenter)

    label_inicio = QLabel("Configuração")
    label_inicio.setFont(QFont("Abril Fatface", 30))
    label_inicio.setStyleSheet("border: none;  padding: 0px;")
    pesquisa_layout.addWidget(label_inicio)

    pesquisa_layout.addStretch()
    content_pesquisa_layout.addWidget(pesquisa_widget)

    # Conteúdo principal
    content_pri_layout = QVBoxLayout()

    content_widget = QWidget()
    content_layout = QVBoxLayout(content_widget)

    label_download = QLabel("Diretório de Download")
    label_download.setFont(QFont("Lato", 15))
    label_download.setStyleSheet("color: white; border: none;")
    content_layout.addWidget(label_download)

    content_layout.addSpacing(5)

    content_layout1 = QHBoxLayout()

    downloads_path = self.load_download_path()

    self.line_download = QLineEdit()
    self.line_download.setStyleSheet("color: white; padding: 5px;")
    self.line_download.setPlaceholderText(str(downloads_path))
    self.line_download.setReadOnly(True)
    self.line_download.setFont(QFont("Lato", 10, QFont.Bold))
    content_layout1.addWidget(self.line_download)

    self.button_selecionar = QPushButton("Selecionar")
    self.button_selecionar.setFont(QFont("Lato", 10))  # Definindo tamanho do botão
    self.button_selecionar.setFixedWidth(100)
    self.button_selecionar.setStyleSheet("color: white; background-color: black; border: 2px solid white")
    self.button_selecionar.clicked.connect(self.OpenFileA)
    content_layout1.addWidget(self.button_selecionar)

    content_layout.addLayout(content_layout1)
    content_layout.addSpacing(20)

    self.button_salvar = QPushButton("Salvar")
    self.button_salvar.setFont(QFont("Lato", 10))
    self.button_salvar.setStyleSheet("color: white; background-color: black; border: 2px solid white")
    self.button_salvar.clicked.connect(lambda: self.save_download_path(Path(self.line_download.text())))

    self.button_salvar.setFixedSize(100,40)
    content_layout.addWidget(self.button_salvar, alignment= Qt.AlignCenter)

    content_layout.addStretch()

    # Adicionar o widget ao layout principal
    content_pri_layout.addWidget(content_widget)
    # Adicionando o layout de conteúdo ao layout principal
    content_pesquisa_layout.addLayout(content_pri_layout)
    
    return content_pesquisa_layout
2