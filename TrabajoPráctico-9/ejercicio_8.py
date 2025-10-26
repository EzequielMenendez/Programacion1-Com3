def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito en un número de forma recursiva.
    """
    # Si el número tiene un solo dígito.
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        # Si el último dígito coincide, sumamos 1 y continuamos con el resto.
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        # Si no coincide, solo continuamos con el resto.
        else:
            return contar_digito(numero // 10, digito)

def ejercicio_8():
    print("====== Ejercicio 8 ======")
    try:
        num = int(input("Ingrese un número entero: "))

        if num < 1:
            print("Entrada no válida. debe ser un número mayor o igual a 1.")
            return

        digito = int(input("Ingrese el dígito a buscar: "))

        if digito > 9:
            print("Entrada no válida. el dígito debe debe ser un caracter.")
            return
        
        print(f"El dígito {digito} aparece {contar_digito(num, digito)} veces en {num}.")

    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")