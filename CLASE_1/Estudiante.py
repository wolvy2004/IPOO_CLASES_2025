class Estudiante:
    
    def __init__(self, nombre:str, apellido:str, notas:list):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas
        
    
    def calcular_promedio(self)->float :  # Método
        return sum(self.notas) / len(self.notas)
    
    def mostrar_informacion(self, nombre:str)->None:  # Método
        self.nombre = nombre
        print(f"Nombre: {self.nombre}")
        print(f"Nombre: {self.apellido}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {self.calcular_promedio():.2f}")


Diego = Estudiante( 'Diego', 'Fierro', [7,8,10]);
Esteban = Estudiante( apellido="Fraccascia", notas=[7,8,10], nombre='Esteban');

print(f"El promedio de las notas de {Diego.nombre} es de {Diego.calcular_promedio()}")
#Diego.mostrar_informacion()
Esteban.apellido = 'Fierro'
Esteban.notas = [5,8,9]
Esteban.mostrar_informacion(nombre="pepito")
print(f"el nombre de el objeto Esteban es  {Esteban.nombre}")