from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea, QGridLayout, QFrame
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

def initUI2(self):

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



    label_inicio = QLabel("Biblioteca")
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
    content_layout1 = QVBoxLayout(content_widget)
     # Espaçamento entre as linhas

    items = [f"Item {i+1}" for i in range(20)]  # Exemplo de 20 itens
    for item in items:

        button = ClickableImageLabel(QPixmap("Imagens/config.png"), 100, 70)
        button.setStyleSheet("border: none; padding: 0px;")

        # Criar um QLabel para ser adicionado ao ClickableImageLabel
        label = QLabel("Nome")
        label.setFont(QFont("Lato", 18, QFont.Bold))
        label.setStyleSheet("border: none; padding: 0px;")

        # Criar um QLabel para ser adicionado ao ClickableImageLabel
        label1 = QPushButton("Abrir")
        label1.setFont(QFont("Lato", 10, QFont.Bold))
        button.setFixedSize(100, 50)
        label1.setFixedWidth(200)
        label1.setStyleSheet("border: 2px solid white; padding: 0px; border-radius: 10px")

        # Criar um frame para conter os elementos
        frame = QFrame()
        frame.setFrameStyle(QFrame.Box | QFrame.Plain)  # Estilo de borda
        frame.setLineWidth(2)  # Largura da borda
        frame_layout = QHBoxLayout(frame)

        # Adicionar os elementos ao layout do frame
        frame_layout.addWidget(button)
        frame_layout.addWidget(label)
        frame_layout.addWidget(label1)

        content_layout1.addWidget(frame)
        content_layout1.addSpacing(10)

    scroll_area.setWidget(content_widget)
    content_pri_layout.addWidget(scroll_area)
    content_pesquisa_layout.addLayout(content_pri_layout)

    
    return content_pesquisa_layout
