# core/settings.py

from pathlib import Path
import json

CONFIG_PATH = Path("data/config.json")

DEFAULT_CONFIG = {
    "idioma": "es",
    "tema": "oscuro",
    "iniciar_con_sistema": False,
    "notificaciones": True
}

def cargar_configuracion():
    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"[ERROR] No se pudo cargar la configuración: {e}")
    guardar_configuracion(DEFAULT_CONFIG)
    return DEFAULT_CONFIG.copy()

def guardar_configuracion(config: dict):
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"[ERROR] No se pudo guardar la configuración: {e}")

def actualizar_configuracion(clave: str, valor):
    config = cargar_configuracion()
    config[clave] = valor
    guardar_configuracion(config)
    return config
