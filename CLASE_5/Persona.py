from abc import ABC, abstractmethod


class Persona(ABC):
    
    identificador:int = 0
    
    def __init__(self, nombre:str, age:int):
      self.autoincrementID()
      self.id = self.identificador
      self.__name = nombre
      self.__age = age
      
    @property
    def name(self)->str:
        return self.__name
      
    @name.setter
    def name(self, nuevo_nombre:str)->None:
        if len(nuevo_nombre)<2:
              print('el nombre debe contener al menos 3 caracteres')
              
        else:
            self.__name = nuevo_nombre
    
    @abstractmethod        
    def __repr__(self) -> str:
        return f'{self.name} edad: {self.__age}'

    
    def autoincrementID(self):
        self.identificador+=1    
    
    