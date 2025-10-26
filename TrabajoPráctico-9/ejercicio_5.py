def es_palindromo(palabra):
    # elimino espacios y convierto a minusculas
    palabra = palabra.replace(" ", "").lower()
    
    # Una palabra de 1 es palíndromo
    if len(palabra) <= 1:
        return True
    else:
        # Si la primera y última letra son iguales, se analiza el resto de la palabra.
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        # Si son diferentes, no es un palíndromo.
        else:
            return False

def ejercicio_5():
    print("====== Ejercicio 5 ======")
    
    palabra = input("Ingrese una palabra: ")
    print(f"{palabra} es palíndromo" if es_palindromo(palabra) else f"{palabra} no es palíndromo")