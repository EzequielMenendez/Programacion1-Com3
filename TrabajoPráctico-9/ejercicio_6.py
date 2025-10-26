def suma_digitos(n):
    # si n es un solo dígito, la suma es n.
    if n < 10:
        return n
    # suma del último dígito más la suma de los restantes.
    else:
        return (n % 10) + suma_digitos(n // 10)

def ejercicio_6():
    print("====== Ejercicio 6 ======")
    try:
        num = int(input("Ingrese un número entero: "))

        if num < 1:
            print("Entrada no válida. Ingrese un número mayor o igual a 1.")
        else:
            print(f"La suma de todos los dígitos es: {suma_digitos(num)}")
    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")