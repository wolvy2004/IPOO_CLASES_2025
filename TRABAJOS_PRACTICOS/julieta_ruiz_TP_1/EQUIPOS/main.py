import Jugadores
import Equipos
import csv
from Jugadores import Jugador
from Equipos import Equipos

datos = []

equip =[]

with open('jugadores.csv', newline='') as csvfile:
    dato = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in dato:
        datos.append(row)

with open('equipos.csv', newline='') as csvfile:
    equipo = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in equipo:
        equip.append(row)
    

jugadores = Jugador(datos)
jugadores.mostrar_jugadores()
jugadores.jugadoresMasAltos()
jugadores.jugadoresConMasPuntos()
jugadores.calcularAlturaPromedio()
equipo = Equipos(equip)
equipo.EquiposMasGanadores()


