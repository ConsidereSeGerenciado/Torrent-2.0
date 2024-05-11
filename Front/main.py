import sys
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyTorrent")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal da janela
        main_layout = QVBoxLayout()
        self.setStyleSheet("background-color: black; color: white;")

        # Área do cabeçalho
        header_widget = QLabel("<font face='Abril Fatface' size='8'><b>PyTorrent</b></font>")
        header_widget.setStyleSheet("border-bottom: 2px solid white; background-color: black;")
        header_widget.setFixedHeight(50)
        header_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        main_layout.addWidget(header_widget)

       # Layout para o conteúdo principal e o menu
        content_menu_layout = QHBoxLayout()

        # Área do menu
        menu_widget = QWidget()
        menu_widget.setStyleSheet("background-color: black; border-right: 2px solid white;")  # Borda branca, fundo preto
        menu_widget.setFixedWidth(100)
        menu_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        # Layout para os botões do menu
        menu_layout = QVBoxLayout(menu_widget)
        menu_layout.setAlignment(Qt.AlignTop)

        menu_layout.addSpacing(10)
        # Botões do menu
        button_home = ClickableImageLabel(QPixmap("Imagens/casa.png"), 40, 40)
        button_home.clicked.connect(self.home_clicked)
        button_home.setStyleSheet("border: none;  padding: 0px;")
        menu_layout.addWidget(button_home, alignment=Qt.AlignCenter)

        menu_layout.addSpacing(15)

        button_tipo = ClickableImageLabel(QPixmap("Imagens/tipos.png"), 40, 40)
        button_tipo.clicked.connect(self.tipo_clicked)
        button_tipo.setStyleSheet("border: none; padding: 0px;")
        menu_layout.addWidget(button_tipo, alignment=Qt.AlignCenter)

        menu_layout.addSpacing(15)

        button_biblioteca = ClickableImageLabel(QPixmap("Imagens/biblioteca.png"), 40, 40)
        button_biblioteca.setStyleSheet("border: none; padding: 0px;")
        button_biblioteca.clicked.connect(self.biblioteca_clicked)
        menu_layout.addWidget(button_biblioteca, alignment=Qt.AlignCenter)

        menu2_layout = QHBoxLayout() 
        menu2_layout.setAlignment(Qt.AlignBottom)  # Define o alinhamento vertical para a parte inferior

        button_github = ClickableImageLabel(QPixmap("Imagens/github.png"),20,20)
        button_github.setStyleSheet("border:none; padding: 0px;")
        button_github.clicked.connect(self.github_clicked)
        menu2_layout.addWidget(button_github, alignment=Qt.AlignCenter)

        button_config = ClickableImageLabel(QPixmap("Imagens/config.png"),20,20)
        button_config.setStyleSheet("border:none; padding: 0px;")
        button_config.clicked.connect(self.config_clicked)
        menu2_layout.addWidget(button_config, alignment=Qt.AlignCenter)
        # Adicione o layout horizontal ao layout vertical do menu
        menu_layout.addStretch()
        menu_layout.addLayout(menu2_layout)

        # Adicionando o menu à área do menu
        content_menu_layout.addWidget(menu_widget)

        # Área da pesquisa
        content_pesquisa_layout = QVBoxLayout() 

        pesquisa_widget = QWidget()
        pesquisa_widget.setStyleSheet("background-color: black; border-bottom: 2px solid white;")  # Borda branca, fundo preto
        pesquisa_widget.setFixedHeight(80)
        pesquisa_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        pesquisa_layout = QHBoxLayout(pesquisa_widget)
        pesquisa_layout.setAlignment(Qt.AlignCenter)

        label_inicio = QLabel("<font face='Abril Fatface' size='8'><b>Início</b></font>")
        label_inicio.setStyleSheet("border: none;  padding: 0px;")
        pesquisa_layout.addWidget(label_inicio, alignment=Qt.AlignCenter)

        pesquisa_layout.addStretch()

        line_edit_busca = QLineEdit()
        line_edit_busca.setStyleSheet("color: white; padding: 5px;")
        line_edit_busca.setPlaceholderText("Buscar")
        line_edit_busca.setFixedWidth(200)
        pesquisa_layout.addWidget(line_edit_busca, alignment=Qt.AlignCenter)

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

        # Adicionando o layout de pesquisa ao layout principal
        content_menu_layout.addLayout(content_pesquisa_layout)

        # Adicionando o layout de conteúdo e menu ao layout principal
        main_layout.addLayout(content_menu_layout)

        # Criando um widget central para conter o layout principal
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def home_clicked(self):
        print("Home clicked")

    def tipo_clicked(self):
        print("Tipo clicked")

    def biblioteca_clicked(self):
        print("Biblioteca clicked")

    def config_clicked(self):
        print("Config clicked")

    def github_clicked(self):
        print("Github clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
