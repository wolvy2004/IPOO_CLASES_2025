import re


class SepararPalabras:
    """Separar palabras"""

    def __init__(self, text):
        print('Comienza SepararPalabras.__init__()')
        self.palabras = text.split()
        print('Finaliza SepararPalabras.__init__()')


class ContarPalabras(SepararPalabras):
    """Count words in text"""

    def __init__(self, text):
        print('Comienza ContarPalabras.__init__()')
        super().__init__(text)
        self.cantidad_palabras = len(self.palabras)
        print('Finaliza ContarPalabras.__init__()')


class Vocabulario(SepararPalabras):
    """Encontrar palabras unicas en el texto"""

    def __init__(self, text):
        print('Comienza init Vocabulario.__init__()')
        super().__init__(text)
        self.vocabulario = set(self.palabras)
        print('Finaliza init Vocabulario.__init__()')


class DescribirTexto(ContarPalabras, Vocabulario):
    """Describe un texto con multiples metricas"""

    def __init__(self, text):
        print('Comienza init DescribirTexto.__init__()')
        super().__init__(text)
        print('Finaliza init DescribirTexto.__init__()')


pattern = r'[A-Za-w]\w+'

texto = "vuela alto: pequeña *Mariposa*, vuela sin cesar mariposa carmesí."
texto_filtrado = re.findall(pattern=pattern, string=texto)
texto = " ".join(texto_filtrado).lower()

describir_texto = DescribirTexto(text=texto)
separador = '\n' + '-' * 25 + '\n'
print('palabras encontradas:', end=separador)
for n in describir_texto.vocabulario:
    print(n, end=', ')
print(separador)
print(f'cantidad de palabras: {describir_texto.cantidad_palabras}')

mro = DescribirTexto.mro()
orden = 1
for n in mro:
    print(f'orden:{orden} {n.__name__}')
    orden += 1
