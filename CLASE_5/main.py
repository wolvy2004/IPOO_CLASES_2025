from Jugador import Jugador
from Calculadora import Calculadora

"""
Keyword arguments:
argument -- dictionary { nombre:str, age:int}
Return: None
"""
def crearJugador(datos_jugador:dict):
    
    jugador = Jugador(nombre=datos_jugador['nombre'], age=datos_jugador['age'], cant_puntos=datos_jugador['cant_puntos'])
    print(jugador.id)
    return jugador


if __name__ == "__main__":
    equipo:list[Jugador]=[]
    nuevo_jugador1 = crearJugador({'nombre':'Hernandez Julian', 'age':21, 'cant_puntos': 180})
    equipo.append(nuevo_jugador1)
    print(equipo)
    nuevo_jugador2 = crearJugador({'nombre':'Hernandez Marcelo', 'age':19, 'cant_puntos': 300})
    equipo.append(nuevo_jugador2)
    print(equipo)
    nuevo_jugador3 = crearJugador({'nombre':'Ivan Julian', 'age':21, 'cant_puntos': 120})
    equipo.append(nuevo_jugador3)
    print(equipo)
    
    print (f' suma {Calculadora.suma(10,60)}')
    print (f' division {Calculadora.division(100, 0)}')