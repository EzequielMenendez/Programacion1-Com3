def decimal_a_binario(n):
    # si n es 0 o 1, su binario es el mismo número.
    if n < 2:
        return str(n)
    # se llama a la función con el cociente y se concatena el resto.
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def ejercicio_4():
    print("====== Ejercicio 4 ======")
    try:
        numero_decimal = int(input("Ingrese un número entero positivo para convertir a binario: "))

        if numero_decimal < 0:
            print("Entrada no válida. Ingrese un número positivo.")
        else:
            resultado_binario = decimal_a_binario(numero_decimal)
            print(f"El número {numero_decimal} en binario es: {resultado_binario}")
            print(f"Prueba con 10: {decimal_a_binario(10)}")
    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")