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

def menu(self):
    # Layout para o conteúdo principal e o menu
    content_menu_layout = QHBoxLayout()

    # Área do menu
    menu_widget = QWidget()
    menu_widget.setStyleSheet("background-color: black; border-right: 2px solid white;")
    menu_widget.setFixedWidth(100)
    menu_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

    # Layout para os botões do menu
    menu_layout = QVBoxLayout(menu_widget)
    menu_layout.setAlignment(Qt.AlignTop)

    menu_layout.addSpacing(10)
    # Botões do menu
    button_home = ClickableImageLabel(QPixmap("Imagens/casa.png"), 512, 512)
    button_home.clicked.connect(self.home_clicked)
    button_home.setFixedSize(50, 50)
    button_home.setStyleSheet("border: none;  padding: 0px;")

    button_home.setContentsMargins(5, 5, 5, 5)

    button_home.setMouseTracking(True)
    button_home.enterEvent = lambda event: self.on_enter(button_home)
    button_home.leaveEvent = lambda event: self.on_leave(button_home)

    menu_layout.addWidget(button_home, alignment=Qt.AlignCenter)

    menu_layout.addSpacing(15)

    button_tipo = ClickableImageLabel(QPixmap("Imagens/tipos.png"), 512, 512)
    button_tipo.clicked.connect(self.tipo_clicked)
    button_tipo.setFixedSize(50, 50)
    button_tipo.setStyleSheet("border: none; padding: 0px;")

    button_tipo.setContentsMargins(5, 5, 5, 5)

    button_tipo.setMouseTracking(True)
    button_tipo.enterEvent = lambda event: self.on_enter(button_tipo)
    button_tipo.leaveEvent = lambda event: self.on_leave(button_tipo)

    menu_layout.addWidget(button_tipo, alignment=Qt.AlignCenter)

    menu_layout.addSpacing(15)

    button_biblioteca = ClickableImageLabel(QPixmap("Imagens/biblioteca.png"), 512, 512)
    button_biblioteca.setStyleSheet("border: none; padding: 0px;")
    button_biblioteca.setFixedSize(50, 50)
    button_biblioteca.clicked.connect(self.biblioteca_clicked)

    button_biblioteca.setContentsMargins(5, 5, 5, 5)

    button_biblioteca.setMouseTracking(True)
    button_biblioteca.enterEvent = lambda event: self.on_enter(button_biblioteca)
    button_biblioteca.leaveEvent = lambda event: self.on_leave(button_biblioteca)

    menu_layout.addWidget(button_biblioteca, alignment=Qt.AlignCenter)

    menu2_layout = QHBoxLayout() 
    menu2_layout.setAlignment(Qt.AlignBottom)  # Define o alinhamento vertical para a parte inferior

    button_github = ClickableImageLabel(QPixmap("Imagens/github.png"),512,512)
    button_github.setStyleSheet("border:none; padding: 0px;")
    button_github.setFixedSize(40, 40)
    button_github.clicked.connect(self.github_clicked)

    button_github.setContentsMargins(10, 10, 10, 10)

    button_github.setMouseTracking(True)
    button_github.enterEvent = lambda event: self.on_enter(button_github)
    button_github.leaveEvent = lambda event: self.on_leave(button_github)

    menu2_layout.addWidget(button_github, alignment=Qt.AlignCenter)

    button_config = ClickableImageLabel(QPixmap("Imagens/config.png"),512,512)
    button_config.setStyleSheet("border:none; padding: 0px;")
    button_config.setFixedSize(40, 40)
    button_config.clicked.connect(self.config_clicked)

    button_config.setContentsMargins(10, 10, 10, 10)

    button_config.setMouseTracking(True)
    button_config.enterEvent = lambda event: self.on_enter(button_config)
    button_config.leaveEvent = lambda event: self.on_leave(button_config)

    menu2_layout.addWidget(button_config, alignment=Qt.AlignCenter)
    # Adicione o layout horizontal ao layout vertical do menu
    menu_layout.addStretch()
    menu_layout.addLayout(menu2_layout)

    # Adicionando o menu à área do menu
    content_menu_layout.addWidget(menu_widget)
    return content_menu_layout