import random
import string
class PasswordAnalizer:
    def __init__(self, numeros= 2, mayusculas = 2, longitudMinima = 8):    
        self.numeros = numeros
        self.mayusculas = mayusculas
        self.longitudMinima = longitudMinima

    def esClaveFuerte(self,clave)->bool:
        cant_numeros = sum(c.isdigit() for c in clave)
        cant_mayusculas = sum(c.isupper() for c in clave)
        longitud = len(clave)
        return(cant_numeros >= self.numeros and cant_mayusculas >= self.mayusculas and longitud >= self.longitudMinima)
        # if (cant_numeros >= self.numeros and cant_mayusculas >= self.mayusculas and longitud >= self.longitudMinima):
        #     return 'Es clave fuerte' 
        # else:
        #     return 'Es clave debil'
    def generarClave(self):
        clave =[]
        numero = "".join(random.choice(string.digits) for _ in range(2))
        letras = string.ascii_letters + string.digits 
        cadena ="".join(random.choice(letras) for _ in range(4))    
        mayusc ="".join(random.choice(letras) for _ in range(2)).upper()
       
        clave = list(numero +cadena+mayusc)
        random.shuffle(clave)
        return "".join(clave)
        
        
         