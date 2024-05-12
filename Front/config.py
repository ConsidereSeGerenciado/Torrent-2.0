from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea, QFrame
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

    label_seta = ClickableImageLabel(QPixmap("Imagens/voltar.png"),512,512)
    label_seta.setStyleSheet("border:none; padding: 0px;")
    label_seta.clicked.connect(self.home_clicked)
    label_seta.setStyleSheet("border-bottom: none; padding: 0px;")
    label_seta.setFixedSize(80,30)
    pesquisa_layout.addWidget(label_seta, alignment=Qt.AlignCenter)

    label_inicio = QLabel("<font face='Abril Fatface' size='8'><b>Configuração</b></font>")
    label_inicio.setStyleSheet("border: none;  padding: 0px;")
    pesquisa_layout.addWidget(label_inicio)

    pesquisa_layout.addStretch()

    line_edit_busca = QLineEdit()
    line_edit_busca.setStyleSheet("color: white; padding: 5px;")
    line_edit_busca.setPlaceholderText("Buscar")
    line_edit_busca.setFixedWidth(200)
    pesquisa_layout.addWidget(line_edit_busca, alignment=Qt.AlignCenter)

    content_pesquisa_layout.addWidget(pesquisa_widget)

    # Conteúdo principal
    content_pri_layout = QVBoxLayout()

    group_widget = QWidget()
    group_layout = QVBoxLayout(group_widget)
    group_layout.setSpacing(5)  # Espaçamento entre os elementos

    label_download = QLabel("Diretório de Download")
    label_download.setStyleSheet("color: white; border: none;")
    group_layout.addWidget(label_download)


    group2_layout = QHBoxLayout()

    line_download = QLineEdit()
    line_download.setStyleSheet("color: white; padding: 5px;")
    line_download.setPlaceholderText("C:/Users/Gabri/Downloads/")
    line_download.setFixedWidth(200)
    group2_layout.addWidget(line_download)

    group2_layout.addSpacing(15)
    # Terceira linha - Botão salvar
    button_salvar = QPushButton("Salvar")
    button_salvar.setFixedSize(50, 20)  # Definindo tamanho do botão
    button_salvar.setStyleSheet("color: white; background-color: black; border: 2px solid white")
    group2_layout.addWidget(button_salvar)

    group2_layout.addStretch()

    group_layout.addLayout(group2_layout)
    
    group_layout.addStretch()
    # Adicionar o widget ao layout principal
    content_pri_layout.addWidget(group_widget)
    # Adicionando o layout de conteúdo ao layout principal
    content_pesquisa_layout.addLayout(content_pri_layout)
    
    return content_pesquisa_layout
2