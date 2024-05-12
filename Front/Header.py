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

def header(self):
     # Layout principal da janela
    main_layout = QVBoxLayout()
    self.setStyleSheet("background-color: black; color: white;")

    # Área do cabeçalho
    header_widget = QWidget()
    header_widget.setStyleSheet("border-bottom: 2px solid white; background-color: black;")
    header_widget.setFixedHeight(50)
    header_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    main2_layout = QHBoxLayout(header_widget)

    name_widget = QLabel("<font face='Abril Fatface' size='8'><b>PyTorrent </b></font>")
    name_widget.setStyleSheet("border-bottom: none;")
    main2_layout.addWidget(name_widget)

    main2_layout.addStretch()

    menos_button =  QPushButton(" – ")
    menos_button.clicked.connect(self.menos_clicked)
    menos_button.setStyleSheet("border-bottom: none; padding: 0px;")

    menos_button.setFixedSize(35, 35)

    font = QFont()
    font.setPointSize(22) 
    menos_button.setFont(font)

    menos_button.setMouseTracking(True)
    menos_button.enterEvent = lambda event: self.on_enter(menos_button)
    menos_button.leaveEvent = lambda event: self.on_leave(menos_button)

    main2_layout.addWidget(menos_button, alignment=Qt.AlignCenter)

    quadrado_button = QPushButton(" □ ")
    quadrado_button.clicked.connect(self.quadrado_clicked)
    quadrado_button.setStyleSheet("border-bottom: none; padding: 0px;")

    quadrado_button.setFixedSize(35, 35)

    font = QFont()
    font.setPointSize(22) 
    font.setBold(True) 
    quadrado_button.setFont(font)

    quadrado_button.setMouseTracking(True)
    quadrado_button.enterEvent = lambda event: self.on_enter(quadrado_button)
    quadrado_button.leaveEvent = lambda event: self.on_leave(quadrado_button)

    main2_layout.addWidget(quadrado_button, alignment=Qt.AlignCenter)

    fecha_button = QPushButton(" X ")
    fecha_button.clicked.connect(self.fechar_clicked)
    fecha_button.setStyleSheet("border-bottom: none; padding: 0px;")

    fecha_button.setFixedSize(35, 35)

    font = QFont()
    font.setPointSize(16)
    fecha_button.setFont(font)

    fecha_button.setMouseTracking(True)
    fecha_button.enterEvent = lambda event: self.on_enter(fecha_button)
    fecha_button.leaveEvent = lambda event: self.on_leave(fecha_button)

    main2_layout.addWidget(fecha_button, alignment=Qt.AlignCenter)

    main_layout.addWidget(header_widget)

    return main_layout
