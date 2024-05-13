from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea, QGridLayout, QSpacerItem
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

def initUI4(self):
   
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

    label_inicio = QLabel("{categoria}")
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
    # Layout principal
    content_pri_layout = QVBoxLayout()

    # Criar a área de rolagem
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    content_widget = QWidget()
    content_layout = QVBoxLayout(content_widget)

    destaques_widget = QLabel("Destaque")
    destaques_widget.setFont(QFont("Lato", 20, QFont.Bold))
    destaques_widget.setStyleSheet("border: none; padding: 0px;")
    content_layout.addWidget(destaques_widget)

    destaque_widget = ClickableImageLabel(QPixmap("Imagens/config.png"), 500, 120)
    destaque_widget.clicked.connect(self.titulo_clicked)
    destaque_widget.setStyleSheet("border:2px solid white; padding: 0px;")
    content_layout.addWidget(destaque_widget, alignment=Qt.AlignCenter)
    content_layout.addSpacing(10)

    populares_widget = QLabel("Populares")
    populares_widget.setFont(QFont("Lato", 20, QFont.Bold))
    populares_widget.setStyleSheet("border: none; padding: 0px;")
    content_layout.addWidget(populares_widget)

    # Widget para conter os itens
    content_layout1 = QGridLayout()

    content_layout1.setHorizontalSpacing(50)  # Espaçamento horizontal entre as imagens
    content_layout1.setVerticalSpacing(20)    # Espaçamento vertical entre as linhas

    # Adicionar itens de exemplo
    items = [f"Item {i+1}" for i in range(20)]  # Exemplo de 20 itens
    row = 0
    col = 0
    for item in items:
        button = ClickableImageLabel(QPixmap("Imagens/config.png"), 270, 90)
        button.clicked.connect(self.titulo_clicked)
        button.setStyleSheet("border:2px solid white; padding: 0px;")
        content_layout1.addWidget(button, row, col)

        # Criar um QLabel para ser adicionado ao ClickableImageLabel
        label = QLabel("Tipo")
        label.setAlignment(Qt.AlignBottom)  # Ajustar o alinhamento do texto
        label.setStyleSheet("border: 1px solid white; padding: 0px; background-color: transparent; border-radius: 10px;")
        spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum) # não entendi bem, mas ele coloca o tipo no canto inferior esquerdo
        label.setFixedSize(label.sizeHint()) # faz com que o tamanho seja do mesmo que a palavra 'tipo'
        button.setLayout(QVBoxLayout())  # Definir um layout para o ClickableImageLabel
        button.layout().addItem(spacer)
        button.layout().addWidget(label)  # Adicionar o QLabel ao layout do ClickableImageLabel

        col += 1
        if col == 2:
            col = 0
            row += 1

    # Definir o layout interno de content_widget como content_layout
    content_layout.addLayout(content_layout1)
    
    # Adicionar content_widget ao scroll_area
    scroll_area.setWidget(content_widget)

    # Adicionar scroll_area ao content_pri_layout
    content_pri_layout.addWidget(scroll_area)
    # Adicionando o layout de conteúdo ao layout principal
    content_pesquisa_layout.addLayout(content_pri_layout)

    return content_pesquisa_layout
