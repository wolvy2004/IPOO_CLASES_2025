class Personaje:
    
    tipo_armas = ['AGUA', 'FUEGO', 'TIERRA', 'AIRE']
    
    def __init__(self,nombre:str, puntos_vida:int=5,  puntos_defensa:int=5, puntos_ataque:int=5):
        self.__nombre = nombre
        self.__puntos_vida = puntos_vida
        self.__puntos_ataque = puntos_ataque
        self.__puntos_defensa = puntos_defensa
        print('personaje creado correctamente')
    
    def __validarTipoArma(self, arma:str)->bool:
        return arma in self.tipo_armas
    
    """
    getters y setters de los atributos    
    
    """
    @property
    def puntos_defensa(self)->int:
        return self.__puntos_defensa
    
    @puntos_defensa.setter
    def puntos_defensa(self, nuevos_puntos_defensa):
        if(nuevos_puntos_defensa<0):
            print('los nuevos_puntos_defensa no deben ser menores a 0')
            return False
        else:
            self.__puntos_defensa = nuevos_puntos_defensa    
            return True
    
    @property
    def puntos_ataque(self)->int:
        return self.__puntos_ataque
    
    @puntos_ataque.setter
    def puntos_ataque(self, nuevos_puntos_ataque):
        if(nuevos_puntos_ataque<0):
            print('los nuevos_puntos_defensa no deben ser menores a 0')
            return False
        else:
            self.__puntos_ataque = nuevos_puntos_ataque    
            return True
    
    
    
    @property
    def nombre(self)->str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre_nuevo)->None:
        if len(nombre_nuevo)<4:
            print('el nombre debe tener mas de 3 caracteres')
            return
        self.__nombre = nombre_nuevo
        
    @property
    def puntos_vida(self)->int:
        return self.__puntos_vida
    
    @puntos_vida.setter
    def puntos_vida(self, puntos_vida:int)->bool:
        if(puntos_vida<0):
            print('los puntos de vida no deben ser menores a 0')
            return False
        else:
            self.__puntos_vida = puntos_vida    
            return True
    
        
    
