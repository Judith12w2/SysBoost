import json
from pathlib import Path

RUTA_USUARIOS = Path("data/usuarios.json")

def cargar_usuarios():
    if not RUTA_USUARIOS.exists():
        return []
    try:
        with open(RUTA_USUARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("[Error] No se pudo cargar usuarios:", e)
        return []
    
def verificar_credenciales(usuario: str, password: str, tipo_requerido: str = None) -> str | None:
    usuarios = cargar_usuarios()
    for u in usuarios:
        if (
            u.get("usuario", "").lower() == usuario.lower()
            and u.get("contraseña") == password
        ):
            tipo_usuario = u.get("tipo", "").lower()
            if tipo_requerido is None or tipo_usuario == tipo_requerido.lower():
                return tipo_usuario
    return None



