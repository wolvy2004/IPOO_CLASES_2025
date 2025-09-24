from __Personaje import Personaje


if __name__== '__main__':
    orco = Personaje( nombre='Black Orc', velocidad=50, fuerza=50, puntos_vida=50)
    orco.nombre = 'olco'
    print(orco.nombre)
    del orco
    print(orco.nombre)
    

    
   

