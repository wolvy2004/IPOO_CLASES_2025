from datetime import datetime

class Hardware:
    
    # definimos todos los atributos como privados
    def __init__(self, nombre:str, fabricante:str, modelo:str, anio_fabricacion:str):
        self.__nombre = nombre
        self.__fabricante =fabricante
        self.__modelo = modelo
        self.__anio_fabricacion = datetime.strptime(anio_fabricacion, "%d/%m/%Y").date()
        
    """ 
    lanzamos un error para que si se ejecuta en el hijo 
    y no se reescribio 
    """  
    def descripcion(self)->str:
        raise "debe implementarse en el hijo"
    
    # damos acceso a los atributos mediante getters
    @property
    def nombre(self)->str:
        return self.__nombre
    
    @property
    def fabricante(self)->str:
        return self.__fabricante
    
    @property
    def anio_fabricacion(self)->str:
        return self.__anio_fabricacion

    @property
    def modelo(self)->str:
        return self.__modelo
    
  