import subprocess
import re
import platform

def buscar_drivers():
    drivers = []
    sistema = platform.system()

    try:
        resultado = subprocess.check_output("driverquery", shell=True, text=True, encoding="latin1")
        lineas = resultado.splitlines()

        marcas = {
            "intel": "Intel",
            "amd": "AMD",
            "nvidia": "NVIDIA",
            "realtek": "Realtek"
        }

        for linea in lineas:
            for clave, fabricante in marcas.items():
                if clave in linea.lower():
                    partes = re.split(r'\s{2,}', linea.strip())
                    if len(partes) >= 3:
                        drivers.append({
                            "nombre": partes[0],
                            "fabricante": fabricante,
                            "estado": "Instalado",
                            "version": partes[-2],
                            "fecha": partes[-1]
                        })

    except subprocess.CalledProcessError as e:
        drivers.append({
            "nombre": "Error al ejecutar driverquery",
            "fabricante": "-",
            "estado": "Error",
            "version": "-",
            "fecha": str(e)
        })
    except Exception as e:
        drivers.append({
            "nombre": "Excepción inesperada",
            "fabricante": "-",
            "estado": "Error",
            "version": "-",
            "fecha": str(e)
        })

    if not drivers:
        drivers.append({
            "nombre": "No se encontraron drivers importantes",
            "fabricante": "-",
            "estado": "Desconocido",
            "version": "-",
            "fecha": "-"
        })

    return drivers
