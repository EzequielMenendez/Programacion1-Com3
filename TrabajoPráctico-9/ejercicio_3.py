def potencia(base, exponente):
    # Si el exponente es 0, retorna 1
    if exponente == 0:
        return 1
    # Si no se aplica recursioón
    else:
        return base * potencia(base, exponente - 1)

def ejercicio_3():
    print("====== Ejercicio 3 ======")
    try:
        base_usuario = int(input("Ingrese el número base: "))
        exponente_usuario = int(input("Ingrese el exponente: "))

        if exponente_usuario < 0:
            print("Entrada no válida. Debes ingresar un exponente positivo.")
        else:
            resultado = potencia(base_usuario, exponente_usuario)
            print(f"{base_usuario} elevado a la {exponente_usuario}: {resultado}")
    except ValueError:
        print("Entrada no válida. Ingrese números enteros.")