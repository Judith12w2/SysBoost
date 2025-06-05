# core/premium.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from core.login_dialog import LoginDialog
from widgets.premium_widget import PremiumWidget

class PaginaPremium(QWidget):
    def __init__(self):
        super().__init__()
        self.autenticado = False
        self.tipo_usuario = None
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        self.label_info = QLabel("🔒 Accede como usuario Premium para ver esta funcionalidad.")
        self.layout.addWidget(self.label_info)

        self.btn_login = QPushButton("Iniciar sesión")
        self.btn_login.clicked.connect(self.iniciar_sesion)
        self.layout.addWidget(self.btn_login)

    def iniciar_sesion(self):
        login = LoginDialog(tipo_requerido="premium")
        if login.exec():
            self.tipo_usuario = login.tipo_usuario
            self.autenticado = True
            self.label_info.setVisible(False)
            self.btn_login.setVisible(False)

            # Añadir el widget funcional después del login
            self.premium_widget = PremiumWidget()
            self.layout.addWidget(self.premium_widget)
        else:
            QMessageBox.warning(self, "Error", "Acceso denegado. Se requieren credenciales premium.")
