from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QMessageBox
from core.logger import leer_registros, borrar_registro, importar_eventos_windows


class RegistrosWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        self.label = QLabel("📁 Registros del sistema")
        self.label.setStyleSheet("font-size: 16px;")
        self.layout.addWidget(self.label)

        self.lista_registros = QListWidget()
        self.layout.addWidget(self.lista_registros)

        self.boton_borrar = QPushButton("🗑️ Eliminar Registro Seleccionado")
        self.boton_borrar.clicked.connect(self.eliminar_registro)
        self.layout.addWidget(self.boton_borrar)

        self.boton_importar = QPushButton("📥 Importar registros del sistema")
        self.boton_importar.clicked.connect(self.importar_registros)
        self.layout.addWidget(self.boton_importar)


        self.cargar_registros()

    def importar_registros(self):
        from core.logger import importar_eventos_windows
        if importar_eventos_windows():
            QMessageBox.information(self, "Importado", "Registros del sistema importados correctamente.")
            self.cargar_registros()
        else:
            QMessageBox.critical(self, "Error", "No se pudieron importar los registros.")


    def cargar_registros(self):
        self.lista_registros.clear()
        registros = leer_registros()
        for reg in registros:
            self.lista_registros.addItem(reg)

    def eliminar_registro(self):
        item = self.lista_registros.currentItem()
        if item:
            texto = item.text()
            if borrar_registro(texto):
                QMessageBox.information(self, "Éxito", "Registro eliminado.")
                self.cargar_registros()
            else:
                QMessageBox.warning(self, "Error", "No se pudo eliminar el registro seleccionado.")
