from pathlib import Path
from password_analyzer import PasswordAnalyzer
from typing import List

def analizarClaves(nombre_archivo: str, analizador: PasswordAnalyzer) -> List[str]:
    """
    Lee un archivo de contraseñas y devuelve una lista de las que son débiles.
    :param nombre_archivo: El nombre del archivo a leer.
    :param analizador: Una instancia de PasswordAnalyzer con los criterios a usar.
    :return: Una lista de contraseñas débiles.
    """
    try:
        with Path(nombre_archivo).open('r', encoding='utf-8') as file:
            claves = [line.strip() for line in file if line.strip()]
            return [clave for clave in claves if not analizador.esClaveFuerte(clave)]
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado.")
        return []
    except Exception as e:
        print(f"Error procesando archivo: {e}")
        return []