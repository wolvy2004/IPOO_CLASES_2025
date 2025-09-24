from A import A
class B(A):
    
    def __init__(self, atributo:str):
        print('comienzo del init de la clase B')
        super().__init__(atributo)
        print('cierre del init de la clase B')
    
    def saludar(self):
        raise "debe ser declarado en el hijo"
    
    def saludar_con_atributo(self):
        print(f'hola desde la clase B con el atributo: {self.atributo}')
    