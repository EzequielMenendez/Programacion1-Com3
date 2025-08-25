import math

#Ejercicio 1
print("------------------------Ejecicio 1------------------------")

print("Hola Mundo!")

#Ejercicio 2
print("------------------------Ejecicio 2------------------------")

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
print("------------------------Ejecicio 3------------------------")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
print("------------------------Ejecicio 4------------------------")

radio = float(input("Ingrese el radio de un círculo: "))
perimetro = 2 * math.pi * radio
area = math.pi * (radio**2)

print(f"El perímetro es {perimetro} y el área es {area}")

#Ejercicio 5
print("------------------------Ejecicio 5------------------------")

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = (segundos / 60) / 60
print(f"Equivale a {horas} horas")

#Ejercicio 6
print("------------------------Ejecicio 6------------------------")

tabla = int(input("Ingrese la tabla de multiplicación a consultar: "))

print(f"{tabla} X 1 = {tabla*1}")
print(f"{tabla} X 2 = {tabla*2}")
print(f"{tabla} X 3 = {tabla*3}")
print(f"{tabla} X 4 = {tabla*4}")
print(f"{tabla} X 5 = {tabla*5}")
print(f"{tabla} X 6 = {tabla*6}")
print(f"{tabla} X 7 = {tabla*7}")
print(f"{tabla} X 8 = {tabla*8}")
print(f"{tabla} X 9 = {tabla*9}")
print(f"{tabla} X 10 = {tabla*10}")

#Ejercicio 7
print("------------------------Ejecicio 7------------------------")

print("Ingrese 2 números distintoas a 0")
num1 = int(input("Primer valor: "))
num2 = int(input("Segundo valor: "))

print(f"{num1} + {num2}: {num1 + num2}")
print(f"{num1} - {num2}: {num1 - num2}")
print(f"{num1} * {num2}: {num1 * num2}")
print(f"{num1} / {num2}: {num1 / num2}")

#Ejercicio 8
print("------------------------Ejecicio 8------------------------")

altura = float(input("Ingrese su altura: "))
peso = float(input("ingrese su peso: "))
indice_masa_corporal = peso / (altura ** 2)

print(f"Su índice de masa corporal es de {indice_masa_corporal}")

#Ejercicio 9
print("------------------------Ejecicio 9------------------------")

celcius = float(input("Ingrese una temperatura en Celsius: "))
fahrenheit = (9/5)*celcius + 32

print(f"Fahrenheit: {fahrenheit}")

#Ejercicio 10
print("------------------------Ejecicio 10------------------------")

print("Ingrese 3 números")
num1 = float(input("Primer valor: "))
num2 = float(input("Segundo valor: "))
num3 = float(input("Tercer valor: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio es de {promedio}")