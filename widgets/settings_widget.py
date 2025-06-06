# widgets/settings_widget.py

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton,
    QMessageBox, QCheckBox
)
import json
from core.settings import cargar_configuracion, guardar_configuracion
from core.themes import aplicar_tema


class SettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuración")
        self.config = cargar_configuracion()

        layout = QVBoxLayout(self)

        # Tema
        self.label_tema = QLabel("Tema")
        self.tema_combo = QComboBox()
        self.tema_combo.addItems(["oscuro", "claro"])
        self.tema_combo.setCurrentText(self.config.get("tema", "oscuro"))

        # Idioma
        self.label_idioma = QLabel("Idioma")
        self.idioma_combo = QComboBox()
        self.idioma_combo.addItems(["es", "en (desarrollo)"])
        self.idioma_combo.setCurrentText(self.config.get("idioma", "es"))

        # Notificaciones
        self.check_notif = QCheckBox("Activar notificaciones")
        self.check_notif.setChecked(self.config.get("notificaciones", True))

        # Iniciar con el sistema
        self.check_auto = QCheckBox("Iniciar con el sistema")
        self.check_auto.setChecked(self.config.get("iniciar_con_sistema", False))

        # Botón guardar
        self.btn_guardar = QPushButton("Guardar configuración")
        self.btn_guardar.clicked.connect(self.guardar_configuracion)

        # Añadir al layout
        layout.addWidget(self.label_tema)
        layout.addWidget(self.tema_combo)
        layout.addWidget(self.label_idioma)
        layout.addWidget(self.idioma_combo)
        layout.addWidget(self.check_notif)
        layout.addWidget(self.check_auto)
        layout.addWidget(self.btn_guardar)

    def guardar_configuracion(self):
        nueva_config = {
            "tema": self.tema_combo.currentText(),
            "idioma": self.idioma_combo.currentText(),
            "notificaciones": self.check_notif.isChecked(),
            "iniciar_con_sistema": self.check_auto.isChecked()
        }

        try:
            guardar_configuracion(nueva_config)
            aplicar_tema(nueva_config["tema"])
            QMessageBox.information(self, "Éxito", "Configuración guardada correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar: {e}")
