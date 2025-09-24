import random
class Equipo:
     
   MAX_JUGADORES = 16
   
   def __init__(self, nombre:str, ciudad:str, partidos_jugados:int, partidos_ganados:int, plantel:list["Jugador"]=[]):
        self.nombre = nombre
        self.ciudad = ciudad
        self.partidos_jugados = partidos_jugados
        self.partidos_ganados = partidos_ganados
        self.__plantel = plantel
        
   def __repr__(self) -> str:
        lista_nombres_jugadores_plantel = [jugador.nombre for jugador in self.__plantel]
        nombres_jugadores_plantel = ", ".join(lista_nombres_jugadores_plantel)
        return f'nombre {self.nombre} partidos ganados {self.partidos_ganados} partidos jugados {self.partidos_jugados}\n__plantel : {nombres_jugadores_plantel}'
   
   @property
   def plantel(self):
       return self.__plantel
   
   
   def getJugadorAleatorio(self):
       index = random.randrange(0, len(self.__plantel)-1)
       return self.__plantel[index]
   
   # RELACION DE AGREGACION
   
   def agregarJugador(self, jugador:"Jugador")->None:
        
            if len(self.__plantel)<= self.MAX_JUGADORES and jugador not in self.__plantel:
                self.__plantel.append(jugador)
                print(f'el jugador {jugador.nombre} fue agregador con exito\n', end='-' * 50 + '\n')
        
            elif jugador in self.__plantel:
                print(f' ⚠️   ERROR: el jugador {jugador.nombre} ya existe en el __plantel\n', end='-' * 50 + '\n')
   
   def eliminarJugador(self, jugador:"Jugador")->None:
       self.__plantel.remove(jugador)



class Jugador:
    def __init__ (self, puntos_totales:int, dni:int, nombre:str, fecha_nacimiento:str, altura:float, equipo  = None):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.altura = altura
        self.__equipo: Equipo | None = equipo
        self.puntos_totales = puntos_totales   
    
    # RELACION DE AGREGACION 
    #    
    def __eq__(self, other) -> bool:
        return isinstance(other, Jugador) and self.dni == other.dni
    
    def __hash__(self) -> int:
        return self.dni
        
    
    @property
    def equipo(self)->Equipo | None:
        return self.__equipo
    
    @equipo.setter
    def equipo(self, nuevo_equipo:Equipo)->None:
        self.__equipo = nuevo_equipo
    
    def __repr__(self) -> str:
        return f'{self.nombre}\n{self.altura}\n{self.equipo}'
        



