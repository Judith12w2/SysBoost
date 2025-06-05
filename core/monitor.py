import psutil
import platform

try:
    import GPUtil
except ImportError:
    GPUtil = None

try:
    import wmi
except ImportError:
    wmi = None


def obtener_estado_sistema():
    estado = {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disco": psutil.disk_usage('/').percent,
        "gpu": None,
        "temp_cpu": None,
        "temp_gpu": None,
        "salud_disco": None
    }

    if GPUtil:
        try:
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]
                if gpu.load is not None:
                    estado["gpu"] = round(gpu.load * 100, 2)
                if gpu.temperature is not None:
                    estado["temp_gpu"] = round(gpu.temperature, 1)
        except Exception as e:
            print(f"[ERROR] Obteniendo GPU con GPUtil: {e}")
            estado["gpu"] = None
            estado["temp_gpu"] = None

    if platform.system() == "Windows" and wmi:
        try:
            w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
            sensores = w.Sensor()
            for sensor in sensores:
                if sensor.SensorType == "Temperature":
                    nombre = sensor.Name.lower()
                    if "cpu" in nombre and estado["temp_cpu"] is None:
                        estado["temp_cpu"] = round(sensor.Value, 1)
                    elif "gpu" in nombre and estado["temp_gpu"] is None:
                        estado["temp_gpu"] = round(sensor.Value, 1)
        except Exception as e:
            print(f"[ERROR] WMI/OpenHardwareMonitor: {e}")

    try:
        uso = estado["disco"]
        if uso > 90:
            estado["salud_disco"] = "Crítico"
        elif uso > 75:
            estado["salud_disco"] = "Alerta"
        else:
            estado["salud_disco"] = "Buena"
    except Exception as e:
        print(f"[ERROR] Salud del disco: {e}")
        estado["salud_disco"] = "Desconocida"

    return estado
