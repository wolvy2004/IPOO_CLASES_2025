# principal.py

import sys
# Importación directa del módulo analizador
from analizador import BasketballAnalyzer


def main():
    """Función principal"""
    try:
        analyzer = BasketballAnalyzer()
        analyzer.generar_reporte()
    except KeyboardInterrupt:
        print("\n⚠️  Ejecución interrumpida por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error en la ejecución: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()