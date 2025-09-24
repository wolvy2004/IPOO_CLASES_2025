class Jugador:
    def __init__ (self, dni, nombre, fecha_nacimiento, altura, equipo, puntos_totales):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.altura = float(altura)
        self.equipo = equipo
        self.puntos_totales = int(puntos_totales)   
    
    def __str__(self):  
        return f"{self.nombre} ({self.equipo})"