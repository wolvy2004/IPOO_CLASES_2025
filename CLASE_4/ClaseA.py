class ClaseA:
    
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
        
    def __repr__(self) -> str:
        return f'nombre {self.nombre}'