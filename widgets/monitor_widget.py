from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QProgressBar,
    QGroupBox, QSizePolicy
)
from PySide6.QtCore import QTimer
from core.monitor import obtener_estado_sistema


class MonitorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monitorización del Sistema")

        layout = QVBoxLayout(self)

        # Barras de progreso
        self.cpu_bar = self._crear_barra("Uso de CPU")
        self.ram_bar = self._crear_barra("Uso de RAM")
        self.disk_bar = self._crear_barra("Uso de Disco")
        self.gpu_bar = self._crear_barra("Uso de GPU")

        # Etiquetas de temperatura y salud
        self.temp_cpu_label = QLabel("Temperatura CPU: -- °C")
        self.temp_gpu_label = QLabel("Temperatura GPU: -- °C")
        self.salud_disco_label = QLabel("Salud del Disco: --")

        # Agrupación de información
        info_group = QGroupBox("Información detallada")
        info_layout = QVBoxLayout()
        info_layout.addWidget(self.temp_cpu_label)
        info_layout.addWidget(self.temp_gpu_label)
        info_layout.addWidget(self.salud_disco_label)
        info_group.setLayout(info_layout)

        # Añadir widgets al layout principal
        for bar in (self.cpu_bar, self.ram_bar, self.disk_bar, self.gpu_bar):
            layout.addWidget(bar["label"])
            layout.addWidget(bar["bar"])
        layout.addWidget(info_group)

        # Timer para actualización
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_monitor)
        self.timer.start(3000)  # cada 3 segundos

        self.actualizar_monitor()

    def _crear_barra(self, titulo):
        label = QLabel(f"{titulo}:")
        barra = QProgressBar()
        barra.setRange(0, 100)
        barra.setTextVisible(True)
        barra.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        return {"label": label, "bar": barra}

    def actualizar_monitor(self):
        datos = obtener_estado_sistema()

        self.cpu_bar["bar"].setValue(int(datos.get("cpu", 0)))
        self.ram_bar["bar"].setValue(int(datos.get("ram", 0)))
        self.disk_bar["bar"].setValue(int(datos.get("disco", 0)))

        gpu_value = datos.get("gpu")
        self.gpu_bar["bar"].setValue(int(gpu_value) if gpu_value is not None else 0)

        self.temp_cpu_label.setText(
            f"Temperatura CPU: {datos.get('temp_cpu', '--')} °C" if datos.get("temp_cpu") else "Temperatura CPU: No detectada"
        )
        self.temp_gpu_label.setText(
            f"Temperatura GPU: {datos.get('temp_gpu', '--')} °C" if datos.get("temp_gpu") else "Temperatura GPU: No detectada"
        )
        self.salud_disco_label.setText(
            f"Salud del Disco: {datos.get('salud_disco', '--')}" if datos.get("salud_disco") else "Salud del Disco: No detectada"
        )
