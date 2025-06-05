# core/registros.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from core.login_dialog import LoginDialog
from widgets.registros_widget import RegistrosWidget

class PaginaRegistros(QWidget):
    def __init__(self):
        super().__init__()
        self.autenticado = False
        self.tipo_usuario = None
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        self.label_info = QLabel("🔒 Accede como Administrador para ver los registros.")
        self.layout.addWidget(self.label_info)

        self.btn_login = QPushButton("Iniciar sesión")
        self.btn_login.clicked.connect(self.iniciar_sesion)
        self.layout.addWidget(self.btn_login)

    def iniciar_sesion(self):
        login = LoginDialog(tipo_requerido="administrador")
        if login.exec():
            self.tipo_usuario = login.tipo_usuario
            self.autenticado = True
            self.label_info.setVisible(False)
            self.btn_login.setVisible(False)

            self.registros_widget = RegistrosWidget()
            self.layout.addWidget(self.registros_widget)
        else:
            QMessageBox.warning(self, "Error", "Acceso denegado. Se requieren credenciales de administrador.")
