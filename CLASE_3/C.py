from B import B
from D import D

class C(D,B):
    
    def __init__(self, atributo:str, texto:str):
        print('comienzo del init de la clase C')
        super().__init__(atributo)
        self.__texto=texto
        print('cierre del init de la clase C')
        
    @property
    def texto(self):
        return self.__texto
    
    def saludar(self):
        print ("HOLA DESDE LA CLASE C LA ULTIMA QUE SE CREO", end= "\n"+ '-' * 50 +"\n" )
    
    
    
    
    

objetoC = C('valor1', 'texto 1')
#print(objetoC.texto)
print(objetoC.saludar())
#print(objetoC.saludar_con_atributo())
