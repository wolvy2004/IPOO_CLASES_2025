# modelos.py

from datetime import datetime

class Jugador:
    def __init__(self, dni, nombre_completo, fecha_nacimiento, altura, equipo, puntos_totales):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = self._parse_date(fecha_nacimiento, nombre_completo)
        self.altura = float(altura)
        self.equipo = equipo.lower().strip()
        self.puntos_totales = int(puntos_totales)

    @staticmethod
    def _parse_date(fecha_str, nombre):
        """Parsea la fecha de nacimiento con manejo de errores mejorado"""
        try:
            return datetime.strptime(fecha_str.strip(), '%Y-%m-%d').date()
        except ValueError:
            print(f"Advertencia: Fecha inválida '{fecha_str}' para {nombre}")
            return None

    def __repr__(self):
        return f"Jugador('{self.nombre_completo}', '{self.equipo}', {self.altura}m, {self.puntos_totales}pts)"


class Equipo:
    def __init__(self, nombre, ciudad, partidos_jugados, partidos_ganados):
        self.nombre = nombre.strip()
        self.ciudad = ciudad.strip()
        self.partidos_jugados = int(partidos_jugados)
        self.partidos_ganados = int(partidos_ganados)
        self.partidos_perdidos = self.partidos_jugados - self.partidos_ganados

    @property
    def porcentaje_victoria(self):
        """Calcula el porcentaje de victorias"""
        if self.partidos_jugados == 0:
            return 0.0
        return round((self.partidos_ganados / self.partidos_jugados) * 100, 2)

    def __repr__(self):
        return f"Equipo('{self.nombre}', {self.partidos_jugados}j, {self.partidos_ganados}g)"