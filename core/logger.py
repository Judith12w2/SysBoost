# core/logger.py

from pathlib import Path
import subprocess

RUTA_LOG = Path("data/logs.txt")

def leer_registros():
    if not RUTA_LOG.exists():
        return []

    try:
        with open(RUTA_LOG, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[ERROR] No se pudieron leer los registros: {e}")
        return []

def borrar_registro(texto):
    if not RUTA_LOG.exists():
        return False

    try:
        with open(RUTA_LOG, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        nuevas_lineas = [linea for linea in lineas if linea.strip() != texto]

        with open(RUTA_LOG, "w", encoding="utf-8") as f:
            f.writelines([line + "\n" for line in nuevas_lineas])

        return True
    except Exception as e:
        print(f"[ERROR] No se pudo eliminar el registro: {e}")
        return False

def importar_eventos_windows(max_eventos=20):
    try:
        comando = [
            "powershell",
            "-Command",
            f"Get-WinEvent -LogName System -MaxEvents {max_eventos} | "
            "Select-Object TimeCreated, Message | "
            "ForEach-Object { $_.TimeCreated.ToString() + ' - ' + $_.Message }"
        ]

        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        if resultado.returncode != 0:
            print(f"[ERROR] Fallo al ejecutar PowerShell: {resultado.stderr}")
            return False

        eventos = resultado.stdout.splitlines()
        eventos = [e.strip() for e in eventos if e.strip()]

        from pathlib import Path
        RUTA_LOG = Path("data/logs.txt")
        with open(RUTA_LOG, "a", encoding="utf-8") as f:
            for evento in eventos:
                f.write(evento + "\n")

        return True
    except Exception as e:
        print(f"[ERROR] No se pudieron importar eventos del sistema: {e}")
        return False

