# themes.py

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication

def aplicar_tema(nombre_tema="oscuro"):
    app = QApplication.instance()
    palette = QPalette()

    if nombre_tema == "claro":
        palette.setColor(QPalette.Window, QColor("#ffffff"))
        palette.setColor(QPalette.WindowText, QColor("#000000"))
        palette.setColor(QPalette.Base, QColor("#f0f0f0"))
        palette.setColor(QPalette.AlternateBase, QColor("#e0e0e0"))
        palette.setColor(QPalette.ToolTipBase, QColor("#ffffff"))
        palette.setColor(QPalette.ToolTipText, QColor("#000000"))
        palette.setColor(QPalette.Text, QColor("#000000"))
        palette.setColor(QPalette.Button, QColor("#e0e0e0"))
        palette.setColor(QPalette.ButtonText, QColor("#000000"))
        palette.setColor(QPalette.BrightText, QColor("#ff0000"))
    else:  # Tema oscuro por defecto
        palette.setColor(QPalette.Window, QColor("#1e1e1e"))
        palette.setColor(QPalette.WindowText, QColor("#ffffff"))
        palette.setColor(QPalette.Base, QColor("#2e2e2e"))
        palette.setColor(QPalette.AlternateBase, QColor("#3c3c3c"))
        palette.setColor(QPalette.ToolTipBase, QColor("#ffffff"))
        palette.setColor(QPalette.ToolTipText, QColor("#ffffff"))
        palette.setColor(QPalette.Text, QColor("#ffffff"))
        palette.setColor(QPalette.Button, QColor("#3c3c3c"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.BrightText, QColor("#ff0000"))

    app.setPalette(palette)
