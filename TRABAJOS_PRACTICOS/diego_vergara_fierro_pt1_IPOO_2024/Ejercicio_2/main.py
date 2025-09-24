from password_analyzer import PasswordAnalyzer
from utils import analizarClaves


def main():
    """
    Función principal para demostrar el uso de los módulos de análisis de contraseñas.
    """
    # Primer analizador
    analizador1 = PasswordAnalyzer(numeros=3, mayusculas=1, longitudMinima=6)
    claves_debiles1 = analizarClaves('claves.txt', analizador1)
    print("Claves débiles (números=3, mayúsculas=1, longitudMinima=6):")
    print(claves_debiles1)

    print("-" * 50)

    # Segundo analizador
    analizador2 = PasswordAnalyzer(numeros=4, mayusculas=3, longitudMinima=12)
    claves_debiles2 = analizarClaves('claves.txt', analizador2)
    print("Claves débiles (números=4, mayúsculas=3, longitudMinima=12):")
    print(claves_debiles2)

    print("-" * 50)

    # Ejemplos de generación
    print(f"Clave generada (criterio 1): {analizador1.generarClave()}")
    print(f"Clave generada (criterio 2): {analizador2.generarClave()}")

    # Verificación
    clave_test = analizador1.generarClave()
    print(f"¿'{clave_test}' es fuerte? {analizador1.esClaveFuerte(clave_test)}")


if __name__ == "__main__":
    main()