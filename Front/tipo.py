from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea, QGridLayout
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

def initUI1(self):
   
    # Área da pesquisa
    content_pesquisa_layout = QVBoxLayout() 

    pesquisa_widget = QWidget()
    pesquisa_widget.setStyleSheet("background-color: #242121; border-bottom: 2px solid white;")
    pesquisa_widget.setFixedHeight(80)
    pesquisa_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    pesquisa_layout = QHBoxLayout(pesquisa_widget)
    pesquisa_layout.setAlignment(Qt.AlignCenter)

    label_seta = ClickableImageLabel(QPixmap("Imagens/voltar.png"),512,512)
    label_seta.setStyleSheet("border:none; padding: 0px;")
    label_seta.clicked.connect(self.home_clicked)
    label_seta.setStyleSheet("border-bottom: none; padding: 0px;")
    label_seta.setFixedSize(50,30)
    pesquisa_layout.addWidget(label_seta, alignment=Qt.AlignCenter)


    label_inicio = QLabel("Tipos de midia")
    label_inicio.setFont(QFont("Abril Fatface", 30))
    label_inicio.setStyleSheet("border: none;  padding: 0px;")
    pesquisa_layout.addWidget(label_inicio, alignment=Qt.AlignCenter)

    pesquisa_layout.addStretch()

    self.line_edit_busca = QLineEdit()
    self.line_edit_busca.setStyleSheet("color: white; padding: 5px;")
    self.line_edit_busca.setPlaceholderText("Buscar")
    self.line_edit_busca.setFont(QFont("Lato", 11, QFont.Bold))
    self.line_edit_busca.setFixedWidth(200)
    self.line_edit_busca.textChanged.connect(self.filtrar_conteudo)
    pesquisa_layout.addWidget(self.line_edit_busca, alignment=Qt.AlignCenter)

    content_pesquisa_layout.addWidget(pesquisa_widget)

    # Conteúdo principal
    content_pri_layout = QVBoxLayout()

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    content_widget = QWidget()
    self.content_layout1 = QGridLayout(content_widget)


    self.content_layout1.setContentsMargins(40,15,0,0)
    self.content_layout1.setHorizontalSpacing(50)
    self.content_layout1.setVerticalSpacing(20)
      
    self.items = [
            ("Jogos", "Imagens/Capas/jogos.jpg"),
            ("Filmes", "Imagens/Capas/filmes.jpg"),
            ("Series", "Imagens/Capas/series.jpg"),
            ("Desenhos", "Imagens/Capas/desenhos.jpg"),
            ("Animes", "Imagens/Capas/animes.jpg"),
            ("Mangas", "Imagens/Capas/mangas.png"),
            ("Musicas", "Imagens/Capas/musica.jpg"),
            ("Livros", "Imagens/Capas/livros.png"),
            ("Software", "Imagens/Capas/software.jpeg")
        ]
    
    self.populate_layout(self.items)
    self.content_layout1.setAlignment(Qt.AlignCenter)

    
    scroll_area.setWidget(content_widget)
    content_pri_layout.addWidget(scroll_area)

    content_pesquisa_layout.addLayout(content_pri_layout)

    
    return content_pesquisa_layout
