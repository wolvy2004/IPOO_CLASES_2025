import random
import string

class PasswordAnalyzer:
    """
    Clase para analizar y generar contraseñas según criterios de fortaleza.
    """
    def __init__(self, numeros=2, mayusculas=2, longitudMinima=8):
        """
        Inicializa el analizador con los criterios de fortaleza.
        :param numeros: Número mínimo de dígitos requeridos.
        :param mayusculas: Número mínimo de letras mayúsculas requeridas.
        :param longitudMinima: Longitud mínima de la contraseña.
        """
        self.numeros = numeros
        self.mayusculas = mayusculas
        self.longitudMinima = longitudMinima

    def esClaveFuerte(self, clave: str) -> bool:
        """
        Verifica si una contraseña cumple con los criterios de fortaleza.
        :param clave: La contraseña a evaluar.
        :return: True si es fuerte, False en caso contrario.
        """
        if not clave or len(clave) < self.longitudMinima:
            return False

        contador_numeros = sum(1 for c in clave if c.isdigit())
        contador_mayusculas = sum(1 for c in clave if c.isupper())

        return (contador_numeros >= self.numeros and
                contador_mayusculas >= self.mayusculas)

    def generarClave(self) -> str:
        """
        Genera una nueva contraseña que cumple con los criterios definidos.
        :return: La contraseña generada.
        """
        # Generar caracteres obligatorios
        clave = (random.choices(string.digits, k=self.numeros) +
                 random.choices(string.ascii_uppercase, k=self.mayusculas))

        # Completar hasta longitud mínima
        restante = self.longitudMinima - len(clave)
        if restante > 0:
            clave.extend(random.choices(string.ascii_letters + string.digits, k=restante))

        random.shuffle(clave)
        return ''.join(clave)