import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout,
    QListWidget, QStackedWidget, QListWidgetItem, QMessageBox
)
from PySide6.QtGui import QIcon
from core.themes import aplicar_tema
from widgets.home import HomeWidget
from widgets.monitor_widget import MonitorWidget
from widgets.optimizer_widget import OptimizerWidget
from widgets.drivers_widget import DriversWidget
from widgets.settings_widget import SettingsWidget
from core.registros import PaginaRegistros
from core.premium import PaginaPremium
import json


class SysBoost(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SysBoost - Optimiza tu sistema")
        self.setWindowIcon(QIcon("data/logo.ico"))
        self.setMinimumSize(1024, 600)

        self.config = self.cargar_configuracion()
        aplicar_tema(self.config.get("tema", "oscuro"))

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        self.menu = QListWidget()
        self.menu.setFixedWidth(200)
        self.secciones = [
            "Inicio", "Monitorización", "Optimización",
            "Drivers", "Registros", "Premium", "Configuración"
        ]
        for texto in self.secciones:
            QListWidgetItem(texto, self.menu)
        self.menu.currentRowChanged.connect(self.cambiar_pagina)

        self.paginas = QStackedWidget()
        self.widget_pages = {}
        self.widgets = {}

        for texto in self.secciones:
            if texto in ["Registros", "Premium"]:
                widget = QWidget()
                self.widgets[texto] = None
            elif texto == "Configuración":
                widget = SettingsWidget()
            elif texto == "Inicio":
                widget = HomeWidget()
            elif texto == "Monitorización":
                widget = MonitorWidget()
            elif texto == "Optimización":
                widget = OptimizerWidget()
            elif texto == "Drivers":
                widget = DriversWidget()

            self.widget_pages[texto] = self.paginas.addWidget(widget)

        layout.addWidget(self.menu)
        layout.addWidget(self.paginas)

        self.menu.setCurrentRow(0)

    def cambiar_pagina(self, index):
        seccion = self.menu.item(index).text()

        if seccion in ["Registros", "Premium"] and self.widgets.get(seccion) is None:
            if seccion == "Registros":
                widget_real = PaginaRegistros()
            elif seccion == "Premium":
                widget_real = PaginaPremium()

            self.widgets[seccion] = widget_real
            self.paginas.removeWidget(self.paginas.widget(self.widget_pages[seccion]))
            self.widget_pages[seccion] = self.paginas.insertWidget(index, widget_real)

        self.paginas.setCurrentIndex(self.widget_pages[seccion])

    def cargar_configuracion(self):
        try:
            with open("data/settings.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"tema": "oscuro"}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = SysBoost()
    app.setWindowIcon(QIcon("data/logo.ico"))
    ventana.show()
    sys.exit(app.exec())
