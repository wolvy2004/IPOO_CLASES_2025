class Equipo:
    def __init__(self, nombre, ciudad, partidos_jugados, partidos_ganados):
        self.nombre = nombre
        self.ciudad = ciudad
        self.partidos_jugados = int(partidos_jugados)
        self.partidos_ganados = int(partidos_ganados)
        
    def partidos_perdidos(self):
        return self.partidos_jugados - self.partidos_ganados
    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"