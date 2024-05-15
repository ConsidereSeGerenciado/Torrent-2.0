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

    line_edit_busca = QLineEdit()
    line_edit_busca.setStyleSheet("color: white; padding: 5px;")
    line_edit_busca.setPlaceholderText("Buscar")
    line_edit_busca.setFont(QFont("Lato", 11, QFont.Bold))
    line_edit_busca.setFixedWidth(200)
    pesquisa_layout.addWidget(line_edit_busca, alignment=Qt.AlignCenter)

    content_pesquisa_layout.addWidget(pesquisa_widget)

    # Conteúdo principal
    content_pri_layout = QVBoxLayout()

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    content_widget = QWidget()
    content_layout1 = QGridLayout(content_widget)

    content_layout1.setHorizontalSpacing(50)  # Espaçamento horizontal entre as imagens
    content_layout1.setVerticalSpacing(20)    # Espaçamento vertical entre as linhas

    # # Adicionar itens de exemplo
    # items = [f"Item {i+1}" for i in range(20)]  # Exemplo de 20 itens
    # row = 0
    # col = 0
    # for item in items:
    #     button = ClickableImageLabel(QPixmap("Imagens/config.png"), 270, 90)
    #     button.clicked.connect(self.genero_clicked)
    #     button.setStyleSheet("border:2px solid white; padding: 0px;")
    #     content_layout1.addWidget(button, row, col)
    #
    #     # Criar um QLabel para ser adicionado ao ClickableImageLabel
    #     label = QLabel("Tipo")
    #     label.setFont(QFont("Abril FatFace", 20, QFont.Bold))
    #     label.setAlignment(Qt.AlignCenter)  # Ajustar o alinhamento do texto
    #     label.setStyleSheet("border: none; padding: 0px; background-color: transparent")
    #     button.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
    #     button.layout().addWidget(label, alignment=Qt.AlignCenter)  # Adicionar o QLabel ao layout do ClickableImageLabel
    #
    #     col += 1
    #     if col == 2:
    #         col = 0
    #         row += 1

    # JOGOS
    button_jogos = ClickableImageLabel(QPixmap("Imagens/Capas/jogos.jpg"), 270, 90)
    button_jogos.clicked.connect(self.genero_clicked)
    button_jogos.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout1.addWidget(button_jogos, 0, 0)

    # Criar um QLabel para ser adicionado ao ClickableImageLabel
    label_jogos = QLabel("Jogos")
    label_jogos.setFont(QFont("Abril FatFace", 20, QFont.Bold))
    label_jogos.setAlignment(Qt.AlignCenter)  # Ajustar o alinhamento do texto
    label_jogos.setStyleSheet("border: none; padding: 0px; background-color: transparent")
    button_jogos.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
    button_jogos.layout().addWidget(label_jogos, alignment=Qt.AlignCenter)  # Adicionar o QLabel ao layout do ClickableImageLabel

    # FILMES
    button_filmes = ClickableImageLabel(QPixmap("Imagens/Capas/filmes.jpg"), 270, 90)
    button_filmes.clicked.connect(self.genero_clicked)
    button_filmes.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout1.addWidget(button_filmes, 0, 1)

    # Criar um QLabel para ser adicionado ao ClickableImageLabel
    label_filmes = QLabel("Filmes")
    label_filmes.setFont(QFont("Abril FatFace", 20, QFont.Bold))
    label_filmes.setAlignment(Qt.AlignCenter)  # Ajustar o alinhamento do texto
    label_filmes.setStyleSheet("border: none; padding: 0px; background-color: transparent")
    button_filmes.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
    button_filmes.layout().addWidget(label_filmes, alignment=Qt.AlignCenter)  # Adicionar o QLabel ao layout do ClickableImageLabel

    # SÉRIES
    button_series = ClickableImageLabel(QPixmap("Imagens/Capas/séries.jpg"), 270, 90)
    button_series.clicked.connect(self.genero_clicked)
    button_series.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout1.addWidget(button_series, 1, 0)

    # Criar um QLabel para ser adicionado ao ClickableImageLabel
    label_series = QLabel("Séries")
    label_series.setFont(QFont("Abril FatFace", 20, QFont.Bold))
    label_series.setAlignment(Qt.AlignCenter)  # Ajustar o alinhamento do texto
    label_series.setStyleSheet("border: none; padding: 0px; background-color: transparent")
    button_series.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
    button_series.layout().addWidget(label_series, alignment=Qt.AlignCenter)  # Adicionar o QLabel ao layout do ClickableImageLabel

    # DESENHOS
    button_desenhos = ClickableImageLabel(QPixmap("Imagens/Capas/desenhos.jpg"), 270, 90)
    button_desenhos.clicked.connect(self.genero_clicked)
    button_desenhos.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout1.addWidget(button_desenhos, 1, 1)

    # Criar um QLabel para ser adicionado ao ClickableImageLabel
    label_desenhos = QLabel("Desenhos")
    label_desenhos.setFont(QFont("Abril FatFace", 20, QFont.Bold))
    label_desenhos.setAlignment(Qt.AlignCenter)  # Ajustar o alinhamento do texto
    label_desenhos.setStyleSheet("border: none; padding: 0px; background-color: transparent")
    button_desenhos.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
    button_desenhos.layout().addWidget(label_desenhos, alignment=Qt.AlignCenter)  # Adicionar o QLabel ao layout do ClickableImageLabel

    # ANIMES
    button_animes = ClickableImageLabel(QPixmap("Imagens/Capas/animes.jpg"), 270, 90)
    button_animes.clicked.connect(self.genero_clicked)
    button_animes.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout1.addWidget(button_animes, 2, 0)

    # Criar um QLabel para ser adicionado ao ClickableImageLabel
    label_animes = QLabel("Animes")
    label_animes.setFont(QFont("Abril FatFace", 20, QFont.Bold))
    label_animes.setAlignment(Qt.AlignCenter)  # Ajustar o alinhamento do texto
    label_animes.setStyleSheet("border: none; padding: 0px; background-color: transparent")
    button_animes.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
    button_animes.layout().addWidget(label_animes, alignment=Qt.AlignCenter)  # Adicionar o QLabel ao layout do ClickableImageLabel

    # MANGÁS
    button_mangas = ClickableImageLabel(QPixmap("Imagens/Capas/mangás.png"), 270, 90)
    button_mangas.clicked.connect(self.genero_clicked)
    button_mangas.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout1.addWidget(button_mangas, 2, 1)

    # Criar um QLabel para ser adicionado ao ClickableImageLabel
    label_mangas = QLabel("Mangás")
    label_mangas.setFont(QFont("Abril FatFace", 20, QFont.Bold))
    label_mangas.setAlignment(Qt.AlignCenter)  # Ajustar o alinhamento do texto
    label_mangas.setStyleSheet("border: none; padding: 0px; background-color: transparent")
    button_mangas.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
    button_mangas.layout().addWidget(label_mangas, alignment=Qt.AlignCenter)  # Adicionar o QLabel ao layout do ClickableImageLabel

    # MÚSICAS
    button_musicas = ClickableImageLabel(QPixmap("Imagens/Capas/música.jpg"), 270, 90)
    button_musicas.clicked.connect(self.genero_clicked)
    button_musicas.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout1.addWidget(button_musicas, 3, 0)

    # Criar um QLabel para ser adicionado ao ClickableImageLabel
    label_musicas = QLabel("Músicas")
    label_musicas.setFont(QFont("Abril FatFace", 20, QFont.Bold))
    label_musicas.setAlignment(Qt.AlignCenter)  # Ajustar o alinhamento do texto
    label_musicas.setStyleSheet("border: none; padding: 0px; background-color: transparent")
    button_musicas.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
    button_musicas.layout().addWidget(label_musicas, alignment=Qt.AlignCenter)  # Adicionar o QLabel ao layout do ClickableImageLabel

    # LIVROS
    button_livros = ClickableImageLabel(QPixmap("Imagens/Capas/livros.png"), 270, 90)
    button_livros.clicked.connect(self.genero_clicked)
    button_livros.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout1.addWidget(button_livros, 3, 1)

    # Criar um QLabel para ser adicionado ao ClickableImageLabel
    label_livros = QLabel("Livros")
    label_livros.setFont(QFont("Abril FatFace", 20, QFont.Bold))
    label_livros.setAlignment(Qt.AlignCenter)  # Ajustar o alinhamento do texto
    label_livros.setStyleSheet("border: none; padding: 0px; background-color: transparent")
    button_livros.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
    button_livros.layout().addWidget(label_livros, alignment=Qt.AlignCenter)  # Adicionar o QLabel ao layout do ClickableImageLabel

    # SOFTWARE
    button_software = ClickableImageLabel(QPixmap("Imagens/Capas/software.jpeg"), 270, 90)
    button_software.clicked.connect(self.genero_clicked)
    button_software.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout1.addWidget(button_software, 4, 0)

    # Criar um QLabel para ser adicionado ao ClickableImageLabel
    label_software = QLabel("Software")
    label_software.setFont(QFont("Abril FatFace", 20, QFont.Bold))
    label_software.setAlignment(Qt.AlignCenter)  # Ajustar o alinhamento do texto
    label_software.setStyleSheet("border: none; padding: 0px; background-color: transparent")
    button_software.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
    button_software.layout().addWidget(label_software, alignment=Qt.AlignCenter)  # Adicionar o QLabel ao layout do ClickableImageLabel
    
    scroll_area.setWidget(content_widget)
    content_pri_layout.addWidget(scroll_area)

    content_pesquisa_layout.addLayout(content_pri_layout)

    
    return content_pesquisa_layout
