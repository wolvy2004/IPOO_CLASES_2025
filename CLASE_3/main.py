from HardwareSalida import HardwareSalida, Hardware


if __name__ == '__main__':
    """
    Instanciamos un objeto de la clase HardwareSalida
    luego imprimimos los datos con el metodo que hereda de su padre el cual
    lo reescribimos, recordar que el original tiene un error para que si lo ejecuten le avisa que 
    debe implementarlo los hijos
    
    para recorrer los atributos de un objeto podemos usar for con el metodo de magico __dict__.items() el cual
    nos devuelve los items del mismo.add()
    
    vamos a tener algunas funciones nativas de Python para poder por ejemplo saber sí un
    objeto es de una clase determinada:
    - isinstance(objeto, clase)  nos retorna True o False si es o no una instancia de un x clase
    esta función es estricta y por ejemplo si el objeto es hijo de otra y queremos validar que sea
    del tipo del padre nos retornara False si preguntamos si es instancia del padre
    - luego podemos saber el tipo con type(objeto)
    - también podemos usar el método mágico objeto.__class__.__name__ que nos devuelve el
      nombre de la clase.   
    
    """
    
    placa_de_video = HardwareSalida(nombre='Placa de Video', fabricante='AMD', modelo='FX7700', anio_fabricacion='10/10/2023', tipo_salida='HDMI' )
    print(placa_de_video.descripcion());
    placa_de_video.tipo_entrada = 'VGA'
    print (type(placa_de_video))
    for  i, n in placa_de_video.__dict__.items():
        print('atributo: {} -->  valor = {}'.format(i, n),end= '\n'+"-"*75 + "\n" )
   
    
    