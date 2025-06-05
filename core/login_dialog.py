# login_dialog.py

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from core.auth import verificar_credenciales

class LoginDialog(QDialog):
    def __init__(self, tipo_requerido="administrador"):
        super().__init__()
        self.setWindowTitle("Iniciar sesión")
        self.tipo_requerido = tipo_requerido
        self.tipo_usuario = None

        self.layout = QVBoxLayout(self)

        self.label_info = QLabel(f"Acceso requerido: {tipo_requerido.capitalize()}")
        self.input_usuario = QLineEdit()
        self.input_usuario.setPlaceholderText("Usuario")

        self.input_contraseña = QLineEdit()
        self.input_contraseña.setPlaceholderText("Contraseña")
        self.input_contraseña.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Iniciar sesión")
        self.btn_login.clicked.connect(self.verificar_login)

        self.layout.addWidget(self.label_info)
        self.layout.addWidget(self.input_usuario)
        self.layout.addWidget(self.input_contraseña)
        self.layout.addWidget(self.btn_login)

    def verificar_login(self):
        usuario = self.input_usuario.text().strip()
        contraseña = self.input_contraseña.text().strip()

        if verificar_credenciales(usuario, contraseña, self.tipo_requerido):
            self.tipo_usuario = self.tipo_requerido
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas o tipo de usuario no autorizado.")
