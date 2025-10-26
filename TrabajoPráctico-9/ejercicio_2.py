def fibonacci(n):
    # Si n es menor a n, retorno n
    if n <= 1:
        return n
    # Si no aplico recursividad
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def ejercicio_2():
    print("====== Ejercicio 2 ======")
    try:
        num = int(input("Ingrese el número de la serie de Fibonacci: "))

        if num < 0:
            print("Entrada no válida. Ingrese un número positivo.")
        else:
            print(f"La serie de Fibonacci hasta la posición {num} es:")
            # Itera y muestra cada número.
            for i in range(num + 1):
                print(fibonacci(i), end=" ")
            print()
    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")