from Hardware import Hardware

class HardwareSalida (Hardware):

        """
        utilizamos el metodo super() el cual nos permite llamar al constructor del padre 
        y pasarle los parametros necesarios.-
        esto es IMPORTANTE porque si bien podriamos inicializarlos en el hijo, 
        si tenemos métodos que necesitan acceder a ellos en/los padres 
        nos va arrojar error.-       
        """

        def __init__(self, nombre:str, fabricante:str, modelo:str, anio_fabricacion:str, tipo_salida:str):
                super().__init__(nombre, fabricante, modelo, anio_fabricacion)
                self.__tipo_salida =tipo_salida


        def descripcion(self)->str:
               return f"Datos del Hardware:\n-------------------\nTipo: {self.nombre}\nFabricante: {self.fabricante}\nModelo: {self.modelo}\nFecha de lanzamiento: {self.anio_fabricacion.strftime('%d/%m/%Y')}\nTipo Salida: {self.tipo_salida}"
                
        @property
        def tipo_salida(self)->str:
            return self.__tipo_salida
        
    