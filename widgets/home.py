# widgets/home_widget.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QFont

class HomeWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        label = QLabel("🔧 Bienvenido a SysBoost")
        label.setFont(QFont("Segoe UI", 20))
        label.setStyleSheet("margin-bottom: 15px;")
        layout.addWidget(label)

        subtitle = QLabel("Optimiza, monitoriza y comprueba tu sistema de forma sencilla. (El programa se encuentra en fase BETA)")
        subtitle.setFont(QFont("Segoe UI", 12))
        subtitle.setStyleSheet("color: gray; margin-bottom: 20px;")
        layout.addWidget(subtitle)

        layout.addStretch()
        self.setLayout(layout)
