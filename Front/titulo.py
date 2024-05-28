from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea, QGridLayout, QSpacerItem, QProgressBar,
)
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import Qt, Signal, QTimer

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

def initUI5(self):
   
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
    label_seta.clicked.connect(self.genero_clicked)
    label_seta.setStyleSheet("border-bottom: none; padding: 0px;")
    label_seta.setFixedSize(50,30)
    pesquisa_layout.addWidget(label_seta, alignment=Qt.AlignCenter)

    label_inicio = QLabel("{nome}")
    label_inicio.setFont(QFont("Abril Fatface", 30))
    label_inicio.setStyleSheet("border: none;  padding: 0px;")
    pesquisa_layout.addWidget(label_inicio, alignment=Qt.AlignCenter)

    pesquisa_layout.addStretch()

    content_pesquisa_layout.addWidget(pesquisa_widget)

    # Conteúdo principal
    # Layout principal
    content_pri_layout = QVBoxLayout()

    # Criar a área de rolagem
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    content_widget = QWidget()
    content_layout = QVBoxLayout(content_widget)
    content_widget.setStyleSheet("border:2px solid white; padding: 0px;")

    logo_widget = ClickableImageLabel(QPixmap("Imagens/config.png"), 600, 120)
    logo_widget.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout.addWidget(logo_widget, alignment=Qt.AlignCenter)
    content_layout.addSpacing(10)

    self.progress_bar = QProgressBar(self)
    self.progress_bar.setGeometry(30, 50, 340, 25)
    self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: transparent;
                border: 1px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: grey;
                width: 10px; /* Largura do preenchimento */
            }
        """)
    self.progress_bar.setVisible(False)
    content_layout.addWidget(self.progress_bar)

    baixar_widget = QPushButton("Baixar")
    baixar_widget.setFont(QFont("Lato", 15, QFont.Bold))
    baixar_widget.setFixedSize(180, 35)
    baixar_widget.setStyleSheet("border: 2px solid white; padding: 0px;")
    baixar_widget.clicked.connect(self.start_progress)
    content_layout.addWidget(baixar_widget, alignment=Qt.AlignCenter)

    self.timer = QTimer(self)
    self.timer.timeout.connect(self.update_progress)
    self.progress_value = 0

    descricao_widget = QLabel("Descrição do titulo")
    descricao_widget.setFont(QFont("Lato", 16, QFont.Bold))
    descricao_widget.setStyleSheet("border: none; padding: 0px;")
    content_layout.addWidget(descricao_widget)

    content_layout.addStretch()

    # Adicionar scroll_area ao content_pri_layout
    content_pri_layout.addWidget(content_widget)
    # Adicionando o layout de conteúdo ao layout principal
    content_pesquisa_layout.addLayout(content_pri_layout)

    return content_pesquisa_layout
