import math

#Ejercicio 1
print("------------------------Ejecicio 1------------------------")

def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo()

#Ejercicio 2
print("------------------------Ejecicio 2------------------------")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

tu_nombre = input("Ingrese su nombre: ")
saludar_usuario(tu_nombre)

#Ejercicio 3
print("------------------------Ejecicio 3------------------------")

def información_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

tu_nombre = input("Ingrese su nombre: ")
tu_apellido = input("Ingrese su apellido: ")
tu_edad = input("Ingrese su edad: ")
tu_residencia = input("Ingrese su residencia: ")
información_personal(tu_nombre, tu_apellido, tu_edad, tu_residencia)

#Ejercicio 4
print("------------------------Ejecicio 4------------------------")

def calcular_area_circulo(radio):
    return math.pi * (radio**2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio_ingresado = float(input("Ingrese el radio de un circulo: "))
print(f"El area es {calcular_area_circulo(radio_ingresado)} y el perímetro es {calcular_perimetro_circulo(radio_ingresado)}")

#Ejercicio 5
print("------------------------Ejecicio 5------------------------")

def segundos_a_horas(segundos):
    horas = (segundos / 60) / 60
    return round(horas, 2)

segundos_ingresados = int(input("Ingrese los segundos que quiera pasar a horas: "))
print(f"{segundos_ingresados} segundos son {segundos_a_horas(segundos_ingresados)} horas")

#Ejercicio 6
print("------------------------Ejecicio 6------------------------")

def tabla_multiplicar(numero):
    print(f"{numero} X 1 = {numero*1}")
    print(f"{numero} X 2 = {numero*2}")
    print(f"{numero} X 3 = {numero*3}")
    print(f"{numero} X 4 = {numero*4}")
    print(f"{numero} X 5 = {numero*5}")
    print(f"{numero} X 6 = {numero*6}")
    print(f"{numero} X 7 = {numero*7}")
    print(f"{numero} X 8 = {numero*8}")
    print(f"{numero} X 9 = {numero*9}")
    print(f"{numero} X 10 = {numero*10}")

tabla = int(input("Ingrese la tabla de multiplicación a consultar: "))
tabla_multiplicar(tabla)

#Ejercicio 7
print("------------------------Ejecicio 7------------------------")

def operaciones_basicas(a, b):
    print(f"{a} + {b}: {a + b}")
    print(f"{a} - {b}: {a - b}")
    print(f"{a} * {b}: {a * b}")
    print(f"{a} / {b}: {a / b}")

print("Ingrese 2 números distintoas a 0")
num1 = int(input("Primer valor: "))
num2 = int(input("Segundo valor: "))
operaciones_basicas(num1, num2)

#Ejercicio 8
print("------------------------Ejecicio 8------------------------")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

altura_ingresada = float(input("Ingrese su altura: "))
peso_ingresado = float(input("ingrese su peso: "))
print(f"Su índice de masa corporal es de {calcular_imc(peso_ingresado, altura_ingresada)}")

#Ejercicio 9
print("------------------------Ejecicio 9------------------------")

def celsius_a_fahrenheit(celsius):
    return (9/5)*celsius + 32

temp_celcius = float(input("Ingrese una temperatura en Celsius: "))
print(f"Fahrenheit: {celsius_a_fahrenheit(temp_celcius)}")

#Ejercicio 10
print("------------------------Ejecicio 10------------------------")

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

print("Ingrese 3 números")
num1 = float(input("Primer valor: "))
num2 = float(input("Segundo valor: "))
num3 = float(input("Tercer valor: "))

print(f"El promedio es de {calcular_promedio(num1, num2, num3)}")