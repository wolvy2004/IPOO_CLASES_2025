class A:
    
    def __init__(self, atributo:str):
        print('comienzo del init de la clase A')
        self.__atributo=atributo
        print('cierre del init de la clase A')
    
    @property
    def atributo(self)->str:
        return self.__atributo
    @atributo.setter
    def atributo(self, nuevo_valor):
        self.__atributo = nuevo_valor
    
    def saludar(self):
        print('hola desde la clase A')
    