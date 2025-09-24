from LectorCSV import LectorCSV
from classes import Jugador , Equipo


class Estadisticas:
    
    # RELACION DE COMPOSICION
    equipos:list[Equipo] = []
    jugadores:list[Jugador]=[]
    
    # RELACION DE DEPENDENCIA
    def __cargarArchivo(self, csv) -> list:
        lector = LectorCSV()
        return lector.CSV_to_list(csv)
        
    # RELACION DE COMPOSICION    
    def crearJugador(self, jugador:list)->Jugador:
        nuevojugador = Jugador(
            dni= int(jugador[4]),
            nombre= jugador[0],
            fecha_nacimiento=jugador[1],
            altura= float(jugador[3]),
            equipo=jugador[2],
            puntos_totales= int(jugador[5]))
        return nuevojugador    
    
    def crearEquipo(self, equipo:list)->Equipo:
        nuevoEquipo = Equipo(
            nombre=equipo[0], ciudad=equipo[1], partidos_ganados=equipo[3], partidos_jugados=equipo[2]
        )
        return nuevoEquipo
        
    def cargarEquipos(self, archivo:str):
        lista_equipos = self.__cargarArchivo(archivo)
        for equipo in lista_equipos:
            equipo_nuevo = self.crearEquipo(equipo=equipo)
            self.equipos.append(equipo_nuevo)
        
                
    def cargasJugadores(self, archivo:str):
        lista_jugadores = self.__cargarArchivo(archivo)
        for jugador in lista_jugadores:
            jugador_nuevo = self.crearJugador(jugador=jugador)
            self.jugadores.append(jugador_nuevo)
    
    
    def jugadoresMasAltos(self)->list:
        altura_max = max(j.altura for j in self.jugadores)
        return [j.nombre for j in self.jugadores if j.altura == altura_max]
        
     
    def equiposMasGanadores(self)->list:
        cant_partidos_ganados = max(equipo.partidos_ganados for equipo in self.equipos )
        return[ equipo.nombre for equipo in self.equipos if equipo.partidos_ganados == cant_partidos_ganados ]
    
    def jugadoresConMasPuntos(self, contador=10)->list:
        max_puntos_totales = max(jugador.puntos_totales for  jugador in self.jugadores )
        return [ jugador.nombre for jugador in self.jugadores if jugador.puntos_totales == max_puntos_totales]
        
    def alturaPromedio(self)->list:
        alturas_promedios:dict ={}
        for equipo in self.equipos:
            alturas_promedios[equipo.nombre] = []
            for jugador in self.jugadores:
                if jugador.equipo == equipo.nombre:
                    alturas_promedios[equipo.nombre].append(jugador.altura)
        return [ {equipo, round(sum(altura)/len(altura), ndigits=2)} for equipo, altura in alturas_promedios.items() if len(altura)>0]        
        
    
    def jugadoresMasPuntosPeorEquipo(self)->list:
        cant_partidos_ganados = min( equipo.partidos_ganados for equipo in self.equipos)
        peor_equipo = [equipo.nombre for equipo in self.equipos if equipo.partidos_ganados == cant_partidos_ganados]
        jugadores = [jugador for jugador in self.jugadores if jugador.equipo in peor_equipo]
        return  [jugador.nombre for jugador in jugadores if jugador.puntos_totales == max(jugador.puntos_totales for jugador in jugadores)]
        
            
    
            
            
            
estadisticas = Estadisticas()

estadisticas.cargasJugadores('jugadores.csv')
estadisticas.cargarEquipos('equipos.csv')

print(estadisticas.jugadoresConMasPuntos())
print(estadisticas.jugadoresMasAltos())
print(estadisticas.equiposMasGanadores())
print(estadisticas.alturaPromedio())
print(estadisticas.jugadoresMasPuntosPeorEquipo())
