import random
from ClaseA import ClaseA

lista = {'equipo1':[1.72, 1.87],'equipo3':[],
         'equipo2':[1.90, 2.07],}


lista1 = []
promedio = [ {equipo, round(sum(promedio)/len(promedio), ndigits=2)} for equipo, promedio in lista.items() if equipo in ['equipo4']]

"""for clave, valor in lista.items():
    promedio = round( sum(valor)/len(valor), ndigits=2)
    print(clave,promedio)"""
print(promedio)

a = ClaseA('uno')
b = ClaseA('dos')
c = ClaseA('tres')

lista1.append(a)
lista1.append(b)

print(lista1)

if c.nombre not in [item.nombre for item in lista1]:
   print('no esta en la lista')
   lista1.append(c)
    
print(random.randint(0, len(lista1)))
print(lista1)




