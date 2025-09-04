print("------------------------------------Ejercicio 1------------------------------------")

for num in range(1, 101):
    print(num)

print("------------------------------------Ejercicio 2------------------------------------")

#Parseo el input a int para asegurar que se ingreso un número
numero = int(input("Ingrese un número: "))
contador = 0
#Recorro cada digíto y sumo 1 al contador
for digito in str(numero):
    contador += 1

print(f"Tu número tiene {contador} digítos")

print("------------------------------------Ejercicio 3------------------------------------")

#Se ingresan los números para hacer la suma
valor1 = int(input("Ingrese el primer valor para la suma: "))
valor2 = int(input("Ingrese el segundo valor para la suma: "))
#Se valida cual es mayor y menor para manejar el range
if valor1 > valor2:
    mayor = valor1
    menor = valor2
else:
    mayor = valor2
    menor = valor1
suma = 0
#Recorro cada número intermedio y lo voy sumando
for num in range(menor+1, mayor):
    suma += num

print(f"La suma entre todos los números comprendidos entre {valor1} y {valor2} es de {suma}")

print("------------------------------------Ejercicio 4------------------------------------")

suma = 0
while True:
    numero = int(input("Ingrese un número a sumar o un 0 si desea salir: "))
    #Si el número ingresado es 0, muestro el resultado y rompo el bucle
    if numero == 0:
        print(f"El total acumulado es de {suma}")
        break
    #Si no, sigo sumando
    suma += numero

print("------------------------------------Ejercicio 5------------------------------------")

import random
#Genero un número random
numero_random = random.randint(0, 9)
numero = -1
contador = 0
#Mientras el número no coincida, pido un nuevo número y sumo 1 intento
while numero != numero_random:
    numero = int(input("Intente adivinar el número aleatorio entre 0 y 9: "))
    contador += 1

print(f"Adivino el número {numero_random} en {contador} intentos")

print("------------------------------------Ejercicio 6------------------------------------")

#Recorro desde 98 para que tome los pares y no tome el 100.
for num in range(98, 0, -2):
    print(num)

print("------------------------------------Ejercicio 7------------------------------------")

numero = int(input("Ingrese un número positivo: "))
#Si el número ingresado es positivo
if(numero > 0):
    suma = 0
    #Ejecuto un for entre 1 y el número positivo y voy sumando los números
    for num in range(1, numero):
        suma += num
    print(f"La suma de los números comprendidos entre 0 y {numero} es de {suma}")
else:
    print("El número no es positivo")

print("------------------------------------Ejercicio 8------------------------------------")

NUMEROS_A_INGRESAR = 100
#Contador
contadores = {"pares": 0, "impares": 0, "positivos": 0, "negativos": 0}

print(f"Ingrese {NUMEROS_A_INGRESAR} números: ")
#Ejecuto un for según los números a ingresar(deben ser 100)
for indice in range(NUMEROS_A_INGRESAR):
    numero = int(input(f"N° {indice+1}: "))
    #Valido si es par o impar y sumo 1 al contador correspondiente
    if(numero % 2 == 0):
        contadores["pares"] += 1
    else:
        contadores["impares"] += 1
    #Valido si es positivo o negativo y sumo 1 al contador correspondiente
    if(numero >= 0):
        contadores["positivos"] += 1
    else:
        contadores["negativos"] += 1

print("Se ingresaron los siguientes valores:")
for contador in contadores:
    print(f"{contador}: {contadores[contador]}")

print("------------------------------------Ejercicio 9------------------------------------")

NUMEROS_A_INGRESAR = 100

suma = 0

print(f"Ingrese {NUMEROS_A_INGRESAR} números: ")
#Ejecuto un for según los números a ingresar(deben ser 100)
for indice in range(NUMEROS_A_INGRESAR):
    numero = int(input(f"N° {indice+1}: "))
    #Acumulo los números en suma
    suma += numero

#Calculo el promedio
promedio = suma / NUMEROS_A_INGRESAR
print(f"El promedio de los números es de {promedio}")

print("------------------------------------Ejercicio 10------------------------------------")

#Parseo el input a int para asegurar que se ingreso un número
numero = int(input("Ingrese un número: "))
numero_inverso = ""
#Recorro cada digíto y lo guardo en un string con orden inverso
for digito in str(numero):
    numero_inverso = digito + numero_inverso

print(numero_inverso)
