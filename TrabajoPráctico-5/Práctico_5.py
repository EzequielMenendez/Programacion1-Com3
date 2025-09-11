print("------------------------------------Ejercicio 1------------------------------------")

#Genero una lista desde el 4 hasta el 101 que avanza en 4
lista_100 = list(range(4, 101, 4))

print(lista_100)

print("------------------------------------Ejercicio 2------------------------------------")

#Recorro la lista en reversa y muestro el penultimo resultado
lista = [1,2,3,4,5]

print(lista[-2:-3:-1])

print("------------------------------------Ejercicio 3------------------------------------")

#Uso append para llenar la lista
lista_vacia = []
lista_vacia.append('UTN')
lista_vacia.append('Práctico')
lista_vacia.append('Listas')

print(lista_vacia)

print("------------------------------------Ejercicio 4------------------------------------")

#Modifico el segundo elemento y el ultimo
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[len(animales) - 1] = "oso"

print(animales)

print("------------------------------------Ejercicio 5------------------------------------")

print("El código primero declara una lista de números,\n"
"luego utiliza el método remove para eliminar un ítem de la lista,\n"
"y ese ítem es el que devuelve la función max,\n"
"que busca el número más grande de una lista,\n"
"por último, muestra la lista modificada")

print("------------------------------------Ejercicio 6------------------------------------")

#lista del 10 al 30 que avanza de 5 en 5, muestro los 2 primeros elementos
lista = list(range(10, 31, 5))
print(lista[0:2])

print("------------------------------------Ejercicio 7------------------------------------")

#cambio las valores de la mitad de la lista calculando con len()
autos = ["sedan", "polo", "suran", "gol"]
longitud = len(autos)
autos[int(longitud / 2)-1] = "Camioneta"
autos[int(longitud / 2)] = "Moto"

print(autos)

print("------------------------------------Ejercicio 8------------------------------------")

#Lleno una lista usando append
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

print("------------------------------------Ejercicio 9------------------------------------")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#Agrego jugo en la tercera lista, remplazo fideos por tallarines en la segunda, y remuevo pan de la primera
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

print("------------------------------------Ejercicio 10------------------------------------")

#Genero una lista anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)