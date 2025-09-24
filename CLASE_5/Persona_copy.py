from abc import ABC, abstractmethod 

# INTERFACE -> EL CONTRATO
class Representacion(ABC):
    
    @abstractmethod
    def __str__(self) -> str:
      pass
             
    @abstractmethod
    def __repr__(self) -> str:
       pass  

#CLASE ABSTRACTA
class Persona(ABC):
    
    def __init__(self, nombre:str, age:int):
      self.__name = nombre
      self.__age = age
    
    @abstractmethod
    def calcularPeso(self)->float:
      pass

#CLASE CONCRETA      
class Jugador(Persona,Representacion):
    
    def __init__(self, nombre: str, age: int, cant_puntos:int):
        super().__init__(nombre, age)
        self.__cantidad_puntos=cant_puntos
        
    def __repr__(self) -> str:
        return f'👱 {self.__name} 🏀 cantidad de puntos : {str(self.__cantidad_puntos)}\n' 
    def __str__(self) -> str:
        return f'👱 {self.__name} 🏀 cantidad de puntos : {str(self.__cantidad_puntos)}\n' 
    
    def calcularPeso(self) -> float:
       return 1.0
    
jugador = Jugador(nombre='nombre', age=38, cant_puntos=150)
