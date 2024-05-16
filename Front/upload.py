from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea, QGridLayout, QSpacerItem, QProgressBar,
    QFileDialog, QComboBox, QTextEdit,
)
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import Qt, Signal, QTimer

class CustomLineEdit(QLineEdit):
    def mousePressEvent(self, event):
        if event.button() == 1:  # Verifica se é o botão esquerdo do mouse
            self.openFileDialog()

    def openFileDialog(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Selecionar Arquivo")
        if file_path:
            self.setText(file_path)

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

def initUI6(self):
   
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

    label_inicio = QLabel("Upload")
    label_inicio.setFont(QFont("Abril Fatface", 30))
    label_inicio.setStyleSheet("border: none;  padding: 0px;")
    pesquisa_layout.addWidget(label_inicio, alignment=Qt.AlignCenter)

    pesquisa_layout.addStretch()

    content_pesquisa_layout.addWidget(pesquisa_widget)

    # Conteúdo principal
    # Layout principal
    content_pri_layout = QVBoxLayout()

    content_widget = QWidget()
    content_layout = QGridLayout(content_widget)
    content_layout.setVerticalSpacing(13)

    nome_widget = QLabel('Nome: ')
    nome_widget.setFont(QFont("Lato", 12))
    content_layout.addWidget(nome_widget,0,0)

    self.nome_widget1 = QLineEdit()
    self.nome_widget1.setStyleSheet("border: 1px solid white; color: white; padding: 5px;")
    self.nome_widget1.setPlaceholderText(" ") 
    content_layout.addWidget(self.nome_widget1,0,1)

    arquivo_widget = QLabel('Arquivo: ')
    arquivo_widget.setFont(QFont("Lato", 12))
    content_layout.addWidget(arquivo_widget,1,0)

    self.directory_edit_arquivo = QLineEdit()
    self.directory_edit_arquivo.setStyleSheet("border: 1px solid white; color: white; padding: 5px;")
    self.directory_edit_arquivo.setReadOnly(True)
    self.directory_edit_arquivo.setPlaceholderText("Caminho do arquivo")
    self.directory_edit_arquivo.setFont(QFont("Lato", 10))
    content_layout.addWidget(self.directory_edit_arquivo,1,1)

    self.select_button = QPushButton("Selecionar")
    self.select_button.setFont(QFont("Lato", 10))
    self.select_button.setStyleSheet("border: 1px solid white; color: white; padding: 5px;")
    self.select_button.clicked.connect(self.openFileDialog)
    content_layout.addWidget(self.select_button,1,2)

    midia_widget = QLabel('Tipo de midia: ')
    midia_widget.setFont(QFont("Lato", 12))
    content_layout.addWidget(midia_widget,2,0)

    self.midia_widget1 = QComboBox()
    self.midia_widget1.addItems(['','Jogos','Filmes','Séries','Desenhos','Animes','Mangás','Músicas','Livros','Software'])
    self.midia_widget1.setFont(QFont("Lato", 10))
    self.midia_widget1.setStyleSheet("border: 1px solid white; color: white; padding: 5px;")
    content_layout.addWidget(self.midia_widget1,2,1)

    imagem_widget = QLabel('Imagem: ')
    imagem_widget.setFont(QFont("Lato", 12))
    content_layout.addWidget(imagem_widget,3,0)

    self.directory_edit_imagem = QLineEdit()
    self.directory_edit_imagem.setStyleSheet("border: 1px solid white; color: white; padding: 5px;")
    self.directory_edit_imagem.setReadOnly(True)
    self.directory_edit_imagem.setPlaceholderText("Caminho do arquivo")
    self.directory_edit_imagem.setFont(QFont("Lato", 10))
    content_layout.addWidget(self.directory_edit_imagem,3,1)

    self.select_button1 = QPushButton("Selecionar")
    self.select_button1.setFont(QFont("Lato", 10))
    self.select_button1.setStyleSheet("border: 1px solid white; color: white; padding: 5px;")
    self.select_button1.clicked.connect(self.openFileDialog1)
    content_layout.addWidget(self.select_button1,3,2)

    descricao_widget = QLabel("Descrição: ")
    descricao_widget.setFont(QFont("Lato", 12))
    content_layout.addWidget(descricao_widget,4,0)
    
    self.descricao_widget1 = QTextEdit ()
    self.descricao_widget1.setFixedHeight(130)
    self.descricao_widget1.setStyleSheet("color: white; padding: 5px;")
    content_layout.addWidget(self.descricao_widget1,4,1)


    content_layout1 = QVBoxLayout()

    self.progress_bar = QProgressBar(self)
    self.progress_bar.setFixedSize(650,30)
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
    content_layout1.addWidget(self.progress_bar, alignment=Qt.AlignCenter)

    self.button_widget = QPushButton("Upload")
    self.button_widget.setFont(QFont("Lato", 15, QFont.Bold))
    self.button_widget.setFixedSize(180, 35)
    self.button_widget.setEnabled(False) 
    self.button_widget.setStyleSheet("border: 2px solid white; padding: 0px; background-color: gray")
    self.button_widget.clicked.connect(self.on_upload_click)
    content_layout1.addWidget(self.button_widget,alignment = Qt.AlignCenter)

    self.timer = QTimer(self)
    self.timer.timeout.connect(self.update_progress)
    self.progress_value = 0

    content_layout1.setAlignment(Qt.AlignCenter)

    content_layout.addLayout(content_layout1, 5, 0, 1, 4)

    self.nome_widget1.textChanged.connect(self.check_fields)
    self.directory_edit_arquivo.textChanged.connect(self.check_fields)
    self.midia_widget1.currentIndexChanged.connect(self.check_fields)
    
    content_pri_layout.addWidget(content_widget)
    # Adicionando o layout de conteúdo ao layout principal
    content_pesquisa_layout.addLayout(content_pri_layout)

    return content_pesquisa_layout
