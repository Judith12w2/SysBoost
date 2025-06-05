from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
)
from PySide6.QtGui import QFont
from core.optimizer import limpiar_temporales, limpiar_descargas


class OptimizerWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        title = QLabel("🧹 Herramientas de Optimización")
        title.setFont(QFont("Segoe UI", 18))
        title.setStyleSheet("margin-bottom: 15px;")
        layout.addWidget(title)

        btn_temp = QPushButton("🗑️ Limpiar archivos temporales")
        btn_temp.clicked.connect(self.ejecutar_limpieza_temporales)
        layout.addWidget(btn_temp)

        btn_descargas = QPushButton("📁 Limpiar carpeta Descargas")
        btn_descargas.clicked.connect(self.pedir_confirmacion_descargas)
        layout.addWidget(btn_descargas)

        layout.addStretch()
        self.setLayout(layout)

    def ejecutar_limpieza_temporales(self):
        resultado = limpiar_temporales()
        QMessageBox.information(
            self, "Limpieza completa",
            f"Archivos eliminados:\n\n"
            f"Temp Usuario: {resultado['temp_usuario']}\n"
            f"Temp Windows: {resultado['temp_windows']}"
        )

    def pedir_confirmacion_descargas(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmación requerida",
            "¿Deseas eliminar el contenido de la carpeta Descargas?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            eliminados = limpiar_descargas(confirmado=True)
            QMessageBox.information(
                self, "Descargas eliminadas",
                f"Se han eliminado {eliminados} elementos de la carpeta Descargas."
            )
