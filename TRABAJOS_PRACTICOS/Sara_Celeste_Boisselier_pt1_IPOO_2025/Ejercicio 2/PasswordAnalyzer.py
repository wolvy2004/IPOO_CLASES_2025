import random
import string

class PasswordAnalyzer:
    def __init__(self, numeros=2, mayusculas=2, longitudMinima=8):
        self.numeros = numeros
        self.mayusculas = mayusculas
        self.longitudMinima = longitudMinima
        
    def esClaveFuerte(self, clave):
        num_count = sum(c.isdigit() for c in clave)
        may_count = sum(c.isupper() for c in clave)
            
        return len(clave) >=self.longitudMinima and num_count >= self.numeros and may_count >= self.mayusculas
        
    def generarClave(self):
        clave = []
        clave.extend(random.choices(string.ascii_uppercase, k=self.mayusculas))
        clave.extend(random.choices(string.digits, k =self.numeros))
        restantes = self.longitudMinima - len(clave)
        if restantes > 0:
            clave.extend(random.choices(string.ascii_lowercase, k=restantes))
        random.shuffle(clave)
        return ''.join(clave)
   
def analizarClaves():
    analizador1 = PasswordAnalyzer(numeros=3, mayusculas=1, longitudMinima=6)
    analizador2 = PasswordAnalyzer(numeros=4, mayusculas=3, longitudMinima=12)
    
    
    with open("claves.txt", "r", encoding="utf-8") as f:
        claves = [line.strip() for line in f if line.strip()]
        
    debiles1 = [clave for clave in claves if not analizador1.esClaveFuerte(clave)]
    debiles2 = [clave for clave in claves if not analizador2.esClaveFuerte(clave)] 
        
    return debiles1, debiles2