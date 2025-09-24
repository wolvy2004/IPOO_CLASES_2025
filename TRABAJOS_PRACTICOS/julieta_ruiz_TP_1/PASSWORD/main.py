import Password
from Password import PasswordAnalizer
with open("claves.txt", "r", encoding="utf-8") as claves:
    contenido = claves.read()
    lista_claves=contenido.split()
    

analizador=PasswordAnalizer()
print(analizador.esClaveFuerte('b15d5TAU'))
print(analizador.generarClave())
def analizarClaves(lista_claves):
    for c in lista_claves:      
        analizador=PasswordAnalizer(3,1,6)
        analizador1=PasswordAnalizer(4,3,12)
        print(analizador.esClaveFuerte(c),c)
       # print(analizador1.esClaveFuerte(c),c)

analizarClaves(lista_claves)