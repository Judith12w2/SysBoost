from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QListWidget, QLineEdit, QHBoxLayout
from core.auth import verificar_credenciales
import subprocess

# Servicios que se pueden deshabilitar sin comprometer el sistema (ejemplo)
SERVICIOS_PERMITIDOS = [
    "Fax", "XblGameSave", "WSearch", "MapsBroker", "DiagTrack", "RetailDemo"
]

class PremiumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.usuario_autenticado = False
        self.tipo_usuario = None

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        self.label = QLabel("🔒 Zona Premium - Gestión de Servicios de Windows")
        self.label.setStyleSheet("font-size: 16px;")
        self.layout.addWidget(self.label)

        self.login_layout = QHBoxLayout()
        self.input_usuario = QLineEdit()
        self.input_usuario.setPlaceholderText("Usuario")
        self.input_contrasena = QLineEdit()
        self.input_contrasena.setPlaceholderText("Contraseña")
        self.input_contrasena.setEchoMode(QLineEdit.Password)

        self.boton_login = QPushButton("Iniciar Sesión")
        self.boton_login.clicked.connect(self.autenticar)

        self.login_layout.addWidget(self.input_usuario)
        self.login_layout.addWidget(self.input_contrasena)
        self.login_layout.addWidget(self.boton_login)
        self.layout.addLayout(self.login_layout)

        self.lista_servicios = QListWidget()
        for servicio in SERVICIOS_PERMITIDOS:
            self.lista_servicios.addItem(servicio)
        self.layout.addWidget(self.lista_servicios)

        self.boton_deshabilitar = QPushButton("🛑 Deshabilitar Servicio Seleccionado")
        self.boton_deshabilitar.clicked.connect(self.deshabilitar_servicio)
        self.boton_deshabilitar.setEnabled(False)
        self.layout.addWidget(self.boton_deshabilitar)

    def autenticar(self):
        usuario = self.input_usuario.text().strip()
        contrasena = self.input_contrasena.text().strip()

        tipo = verificar_credenciales(usuario, contrasena)
        if tipo:
            self.usuario_autenticado = True
            self.tipo_usuario = tipo
            QMessageBox.information(self, "Éxito", f"Bienvenido, {usuario}.")
            self.boton_deshabilitar.setEnabled(True)
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas")

    def deshabilitar_servicio(self):
        if not self.usuario_autenticado:
            QMessageBox.warning(self, "Acceso denegado", "Inicia sesión como usuario premium.")
            return

        item = self.lista_servicios.currentItem()
        if item:
            servicio = item.text()
            try:
                subprocess.run(["sc", "stop", servicio], capture_output=True)
                subprocess.run(["sc", "config", servicio, "start=", "disabled"], capture_output=True)
                QMessageBox.information(self, "Servicio deshabilitado", f"Servicio '{servicio}' deshabilitado.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo deshabilitar el servicio:\n{e}")
        else:
            QMessageBox.warning(self, "Ningún servicio seleccionado", "Selecciona un servicio para deshabilitar.")
