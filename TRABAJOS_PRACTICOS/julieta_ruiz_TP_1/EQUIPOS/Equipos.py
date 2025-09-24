#  nombre
#  • ciudad
#  • partidos jugados
#  • partidos ganados.
class Equipos:
    def __init__(self,lista):
        self.lista=lista
        # self.nombre = nombre
        # self.ciudad = ciudad
        # self.jugados = jugados
        # self.ganados = ganados

     
    def EquiposMasGanadores(self):
        ganador = max(equipos[3] for equipos in self.lista)
        for equipo in self.lista:
            if equipo[3] == ganador:
                print(f'{equipo[0]} es el equipo con mas puntos ganados con un total de {ganador} ')   
                break  

    


