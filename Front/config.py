from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea
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
    pesquisa_widget.setStyleSheet("background-color: black; border-bottom: 2px solid white;") 
    pesquisa_widget.setFixedHeight(80)
    pesquisa_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    pesquisa_layout = QHBoxLayout(pesquisa_widget)

    label_seta = ClickableImageLabel(QPixmap("Imagens/voltar.png"),40,30)
    label_seta.setStyleSheet("border:none; padding: 0px;")
    label_seta.clicked.connect(self.home_clicked)
    label_seta.setStyleSheet("border-bottom: none; padding: 0px;")
    label_seta.setFixedSize(80,30)
    pesquisa_layout.addWidget(label_seta)

    label_inicio = QLabel("<font face='Abril Fatface' size='8'><b>Configuração</b></font>")
    label_inicio.setStyleSheet("border: none;  padding: 0px;")
    pesquisa_layout.addWidget(label_inicio)

    content_pesquisa_layout.addWidget(pesquisa_widget)

    # Conteúdo principal
    content_pri_layout = QVBoxLayout()

    content_widget = QLabel("Conteúdo Principal\n" * 50)
    content_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    scroll_area = QScrollArea()
    scroll_area.setWidget(content_widget)
    scroll_area.setWidgetResizable(True)  # Permitir que o widget se expanda com a área de rolagem

# Adicionar a área de rolagem ao layout do conteúdo principal
    content_pri_layout.addWidget(scroll_area)

    # Adicionando o layout de conteúdo ao layout principal
    content_pesquisa_layout.addLayout(content_pri_layout)

    
    return content_pesquisa_layout
