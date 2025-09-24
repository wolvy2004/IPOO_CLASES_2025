class Calculadora:
    
    @staticmethod
    def suma(a:int | float , b:int | float)->int|float:
        return a + b
    
    @staticmethod
    def resta(a:int | float , b:int | float)->int|float:
        return a - b
    
    @staticmethod
    def multiplicacion(a:int | float , b:int | float)->int|float:
        return a * b
    
    @staticmethod
    def division(a:int | float , b:int | float)-> int | float:
        try: 
            return a / b
        except ZeroDivisionError as e:
            print( f' ⁉️ Error el dividir no se puede dividir por 0 ({e}) ')
            return 0