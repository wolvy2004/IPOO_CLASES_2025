import re
class Personaje:
    
    __nombre='Personaje por defecto'
    _fueza_ = 10
    velocidad = 10
    puntos_vida=10
     
    def __init__(self, nombre:str='Personaje sin nombre', velocidad:int=20, fuerza:int=20, puntos_vida:int=20):
        self.__nombre=nombre
        self._fuerza=fuerza
        self.velocidad= velocidad
        self.puntos_vida=puntos_vida
    def __str__(self)->str:
        return f'nombre del personaje {self.__nombre} \nFuerza: {self._fuerza} ptos \nVelocidad: {self.velocidad} ptos\npuntos de vida: {self.puntos_vida} \npuntos de daño: {self.__calcular_fuerza()}'
    def __calcular_fuerza(self)->int:
        return self._fuerza *  self.puntos_vida
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevoNombre:str)->None:
        if len(nuevoNombre)>3:
            self.__nombre=nuevoNombre
        else:
            print('el nombre deber contener al menos 4 caracteres')
            
    def __del__(self):
        print('clase destruida')

 