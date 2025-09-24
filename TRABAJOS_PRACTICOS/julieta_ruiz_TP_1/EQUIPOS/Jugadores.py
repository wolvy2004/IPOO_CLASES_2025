
# Clase JUGADOR
#  De los jugadores necesitamos saber el dni, nombre completo, fecha de 
# nacimiento, altura, equipo y puntos totales
class Jugador():
    def __init__(self,lista):
        self.lista=lista
        # self.nombre = nombre
        # self.fechaNac = fechaNac
        # self.equipo = equipo
        # self.altura = altura
        # self.DNI = DNI
        # self.puntosTot = puntosTot

    def mostrar_jugadores(self):
        for i, lista in enumerate (self.lista):
            print(i, lista)
    
    def jugadoresMasAltos(self):
        altura_max = max(jugador[3] for jugador in self.lista)
        for jugador in self.lista:
            if jugador[3] == altura_max:
                print(f'El jugador mas alto es {jugador[0]} con una altura de {altura_max} ')   
                break  

    
    def jugadoresConMasPuntos(self):
        
        jugadores = self.lista[:]
        
        for i in range(len(jugadores)):
            for j in range(i+1, len(jugadores)):
                if jugadores[j][5] > jugadores[i][5]:  
                    jugadores[i], jugadores[j] = jugadores[j], jugadores[i]  


        for i in range(min(10, len(jugadores))):
            jugador = jugadores[i]
            print(f"{i+1}. {jugador[0]} - Puntos: {jugador[5]}")

    def calcularAlturaPromedio(self):
        equipos = {}
        for jugador in self.lista:
            equipo = jugador[2]
            altura = jugador[3]
            if equipo not in equipos:
                equipos[equipo] =[]
            equipos[equipo].append(float(altura))

        for equipo, altura in equipos.items():
            promedio = sum(altura)/len(altura)
            print(f'la altura promedio del equipo {equipo} es: {promedio:.2f}')
            