import random

numeros_carton = random.sample(range(1, 51), 25)
carton = [numeros_carton[i:i+5] for i in range(0, 25, 5)]

numeros_sortear = random.sample(range(1, 51), 50)

print("Tu cartón es:")
for columna in carton:
    print(columna)

for num_sorteo in numeros_sortear:
    print(f"Se sortea el número... {num_sorteo}")
    for columna in carton:
        if num_sorteo in columna:
            print("¡Lo tenes!")
            indice_columna = carton.index(columna)
            for valor in columna:
                if valor == num_sorteo:
                    indice_valor = carton[indice_columna].index(valor)
                    carton[indice_columna][indice_valor] = 0
            if columna == [0 for _ in range(5)]:
                print("¡Línea completa!")

    print("Tu cartón es:")
    for columna in carton:
        print(columna)

    if carton == [[0 for _ in range(5)] for _ in range(5)]:
        print("¡Bingo!")
        break
