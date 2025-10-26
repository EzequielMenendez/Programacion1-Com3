def contar_bloques(n):
    # si el nivel más bajo tiene 1 bloque, retorno 1.
    if n == 1:
        return 1
    # n + el total de bloques de una pirámide de base (n-1).
    else:
        return n + contar_bloques(n - 1)

def ejercicio_7():
    print("====== Ejercicio 7 ======")
    try:
        num = int(input("Ingrese un número entero: "))

        if num < 1:
            print("Entrada no válida. ingrese un número mayor o igual a 1.")
        else:
            print(f"Bloques para una base de 1:: {contar_bloques(num)}") 
    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")