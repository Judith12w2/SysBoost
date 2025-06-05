from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, QMessageBox
)
from PySide6.QtGui import QFont
from core import drivers


class DriversWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(15)

        self.layout().addWidget(self.crear_titulo("🛠️ Comprobación de Drivers"))

        self.info_label = QLabel("Pulsa el botón para escanear tu sistema.")
        self.layout().addWidget(self.info_label)

        self.lista_drivers = QListWidget()
        self.layout().addWidget(self.lista_drivers)

        self.boton_buscar = QPushButton("🔍 Buscar drivers desactualizados")
        self.boton_buscar.clicked.connect(self.escanear_drivers)
        self.layout().addWidget(self.boton_buscar)

    def crear_titulo(self, texto):
        label = QLabel(texto)
        label.setFont(QFont("Segoe UI", 18))
        return label

    def escanear_drivers(self):
        self.lista_drivers.clear()
        encontrados = drivers.buscar_drivers()

        if not encontrados:
            QMessageBox.information(self, "Drivers", "✅ Todos los drivers están actualizados.")
            return

        for item in encontrados:
            QListWidgetItem(f"{item['nombre']} - {item['estado']}", self.lista_drivers)
