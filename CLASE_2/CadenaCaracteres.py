
class CadenaCaracteres:
    pass

    def leerArchivo()->None:
        with open('lista_frutas_verduras.csv', 'r') as archivo:
            for  i, n in enumerate(archivo.readlines()):
                item = n.replace('\n', '').split(',')
                texto ='{}- Producto {} precio {}'.format(i, item[0], item[1])
                separador = '\n' + '-' * len(texto)  
                print(f'{texto}  {separador}')
                
            
            


cadena = CadenaCaracteres

cadena.leerArchivo()