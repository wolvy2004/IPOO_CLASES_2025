import csv
from jugador import Jugador
from equipo import Equipo
import funciones as f

def cargar_jugadores(archivo):
    jugadores = []
    with open(archivo, newline='', encoding="utf-8") as csvfile:
        # nombres de columnas según el orden de tu CSV
        fieldnames = ["nombre","fecha_nacimiento","equipo","altura","dni","puntos_totales"]
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            jugador = Jugador(
                row["dni"],
                row["nombre"],
                row["fecha_nacimiento"],
                float(row["altura"]),        # convertimos a float
                row["equipo"],
                int(row["puntos_totales"])   # convertimos a int
            )
            jugadores.append(jugador)
    return jugadores

def cargar_equipos(archivo):
    equipos = []
    with open(archivo, newline='', encoding="utf-8") as csvfile:
        fieldnames = ["nombre","ciudad","partidos_jugados","partidos_ganados"]
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            equipo = Equipo(
                row["nombre"],
                row["ciudad"],
                int(row["partidos_jugados"]),
                int(row["partidos_ganados"])
            )
            equipos.append(equipo)
    return equipos

if __name__ == "__main__":
    jugadores = cargar_jugadores("2025-TR-jugadores.csv")
    equipos = cargar_equipos("2025-TR-equipos.csv") 
    
    print("Jugadores más altos:", f.jugadoresMasAltos(jugadores))
    print("Equipos más ganadores:", f.equiposMasGanadores(equipos))
    print("Top 10 jugadores con más puntos:", f.jugadoresConMasPuntos(jugadores))
    print("Altura promedio por equipo:", f.alturaPromedio(jugadores))
    print("Jugador/es con más puntos en el peor equipo:", f.jugadoresMasPuntosPeorEquipo(jugadores, equipos))
