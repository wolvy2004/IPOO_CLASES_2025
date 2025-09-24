from Persona import Persona
class Jugador(Persona):
    
    def __init__(self, nombre: str, age: int, cant_puntos:int):
        super().__init__(nombre, age)
        self.__cantidad_puntos=cant_puntos
        
    def __repr__(self) -> str:
        return f'id: {self.id} 👱 {self.name} 🏀 cantidad de puntos : {str(self.__cantidad_puntos)}\n' 