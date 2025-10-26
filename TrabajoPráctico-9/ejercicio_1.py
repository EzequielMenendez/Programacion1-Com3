def factorial(n):
    # Si n es 1, retorna 1
    if n <= 1:
        return 1
    # Si no, aplica recursión
    else:
        return n * factorial(n - 1)

def ejercicio_1():
    print("====== Ejercicio 1 ======")
    try:
        numero_limite = int(input("Ingrese un número entero: "))

        if numero_limite < 1:
            print("Entrada no válida. Ingrese un número mayor o igual a 1.")
        else:
            # Itera desde 1 hasta el número ingresado.
            for i in range(1, numero_limite + 1):
                print(f"El factorial de {i} es: {factorial(i)}")
    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")