# core/optimizer.py

import os
import shutil
from pathlib import Path

TEMP_USER = Path(os.getenv("LOCALAPPDATA")) / "Temp"
TEMP_WINDOWS = Path(os.environ.get("WINDIR", "C:\\Windows")) / "Temp"
DOWNLOADS = Path.home() / "Downloads"


def eliminar_contenido_directorio(ruta: Path) -> int:
    archivos_eliminados = 0
    if not ruta.exists():
        return archivos_eliminados

    for item in ruta.iterdir():
        try:
            if item.is_file() or item.is_symlink():
                item.unlink()
                archivos_eliminados += 1
            elif item.is_dir():
                shutil.rmtree(item, ignore_errors=True)
                archivos_eliminados += 1
        except Exception as e:
            print(f"[Error] No se pudo eliminar {item}: {e}")
    return archivos_eliminados


def limpiar_temporales() -> dict:
    resultado = {
        "temp_usuario": eliminar_contenido_directorio(TEMP_USER),
        "temp_windows": eliminar_contenido_directorio(TEMP_WINDOWS)
    }
    return resultado


def limpiar_descargas(confirmado: bool = False) -> int:
    if confirmado:
        return eliminar_contenido_directorio(DOWNLOADS)
    return 0
