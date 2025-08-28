#Ejercicio 1
print("--------------------Ejercicio 1--------------------")

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")

#Ejercicio 2
print("--------------------Ejercicio 2--------------------")

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
print("--------------------Ejercicio 3--------------------")

par = int(input("Ingrese un número par: "))

if par % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
print("--------------------Ejercicio 4--------------------")

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("menor de 12 años")
elif edad < 18:
    print("mayor o igual que 12 años y menor que 18 años.")
elif edad < 30:
    print(" mayor o igual que 18 años y menor que 30 años.")
elif edad >= 30:
    print("mayor o igual que 30 años.")

#Ejercicio 5
print("--------------------Ejercicio 5--------------------")

clave = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

if len(clave) >= 8 and len(clave) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
print("--------------------Ejercicio 6--------------------")

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = round(median(numeros_aleatorios))
media = round(mean(numeros_aleatorios))

if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")

#Ejercicio 7
print("--------------------Ejercicio 7--------------------")

cadena = input("Ingrese una palabra: ")
#Verifico si el ultimo caracter de la cadena tiene una vocal
if cadena[-1].lower() in "aeiou":
    cadena += "!"

print(cadena)

#Ejercicio 8
print("--------------------Ejercicio 8--------------------")

nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese un número según la operación que desee realizar\n1 si quiere su nombre en MAYÚSCULAS\n2 si quiere su nombre en minúsculas\n3 Si quiere su nombre con la primera letra mayúscula\nSu respuesta aquí: "))

if numero == 1:
    nombre = nombre.upper()
elif numero == 2:
    nombre = nombre.lower()
elif numero == 3:
    nombre.title()
else:
    print("Operación incorrecta")
    nombre = ""

print(nombre)

#Ejercicio 9
print("--------------------Ejercicio 9--------------------")

magnitud = float(input("Ingrese la magnitud de un terremoto"))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
elif magnitud >= 7:
    print("Extremo")

#Ejercicio 10
print("--------------------Ejercicio 10--------------------")

hemiferio = input("Ingrese en que hemiferio se encuentra (N/S): ").upper()
#Defino unos arrays de Meses y Días
MESES = range(1,13)
DIAS = range(1, 32)

#Según el hemiferio utilizado guardo las estaciones en un diccionario
if hemiferio == "N":
    estaciones = {1: "Invierno", 2: "Primavera", 3: "Verano", 4: "Otoño"}
elif hemiferio == "S":
    estaciones = {1: "Verano", 2: "Otoño", 3: "Invierno", 4: "Primavera"}
else:
    print("Hemiferio invalido")

#Se ingresa una fecha en formato dd/mm y la divido en 2 variables
fecha = input("Ingrese que mes y día del año es (DD/MM): ")
DD = int(fecha.split("/")[0])
MM = int(fecha.split("/")[1])

#Valido que la fecha sea valida
if DD in DIAS and MM in MESES:
    #Valido en que estación se encuentra y la muestro por pantalla
    if (MM == 12 and DD >= 21) or (MM == 3 and DD <= 20) or (MM >= 1 and MM <= 2):
        print(estaciones[1])
    elif (MM == 3 and DD >= 21) or (MM == 6 and DD <= 20) or (MM >= 4 and MM <= 5):
        print(estaciones[2])
    elif (MM == 6 and DD >= 21) or (MM == 9 and DD <= 20) or (MM >= 7 and MM <= 8):
        print(estaciones[3])
    else:
        print(estaciones[4]) 
else:
    print("fecha invalida")