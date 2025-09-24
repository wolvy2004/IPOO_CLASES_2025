from classes import Jugador, Equipo


jugador1 = Jugador(
    dni=12454578741,
    nombre="Michael Jordan",
    fecha_nacimiento="01-06-1970",
    altura=2.00,
    puntos_totales=0
)  

equipo = Equipo(nombre='Chicago Bulls', ciudad="Chicago", partidos_ganados=0, partidos_jugados=0)   
equipo.agregarJugador(jugador1)
equipo.agregarJugador(jugador1)  # no lo agrega dos veces

print(equipo)
print(equipo.plantel)

jugador1 = Jugador(dni=12454578741, nombre="Michael Jordan", fecha_nacimiento="01-06-1970", altura=2.00, puntos_totales=0)  
equipo = Equipo(nombre='Chicago Bull', ciudad="Chicago", partidos_ganados=0, partidos_jugados=0)
jugador1.equipo = equipo      
print(jugador1 )

equipo.agregarJugador(jugador1)
equipo.agregarJugador(jugador1)

print(equipo)
