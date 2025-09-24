from PasswordAnalyzer import PasswordAnalyzer, analizarClaves

if __name__ == "__main__":
    debiles1, debiles2 = analizarClaves()
    
    print("Claves débiles con analizador 1 (números=3, mayúsculas=1, longitud mínima=6)")
    for c in debiles1:
        print(c)
    
    print("\nClaves débiles con analizador 2 (números=4, mayúsculas=3, longitud mínima=12):")
    for c in debiles2:
        print(c)
        