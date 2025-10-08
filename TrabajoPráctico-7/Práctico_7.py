print("------------------------------------Ejercicio 1------------------------------------")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

print("------------------------------------Ejercicio 2------------------------------------")

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

print("------------------------------------Ejercicio 3------------------------------------")

frutas = list(precios_frutas.keys())

print(frutas)

print("------------------------------------Ejercicio 4------------------------------------")

contactos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del contacto número {i + 1}: ")
    numero = input(f"Ingrese el número del contacto número {i + 1}: ")
    contactos[nombre] = numero

busqueda = input(f"Ingrese el contacto que desea buscar: ")

if busqueda in contactos.keys():
    print(contactos[busqueda])
else:
    print("No se encontro el contacto.")

print("------------------------------------Ejercicio 5------------------------------------")

#Guardo la frase del usuario y la separo por espacios
frase = input("Ingrese una frase: ")
lista_palabras = frase.split(" ")
#Genero el set y recorro las palabras para contarlas
palabras_unicas = set(lista_palabras)
conteo_palabras = {}
for palabra in lista_palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

print(palabras_unicas)
print(conteo_palabras)

print("------------------------------------Ejercicio 6------------------------------------")

try:
    alumnos = {}
    #Se hace un for para cargar los usarios
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno número {i + 1}: ")
        notas = []
        #Se ingresan las notas, las guardo y lo transformo a tupla
        for i in range(3):
            nota = int(input(f"Ingrese la nota número {i + 1} del alumno {nombre}: "))
            notas.append(nota)
        notas = tuple(notas)
        alumnos[nombre] = notas

    #Recorro los alumnos y sus notas para mostrar el promedio
    for alumno in alumnos:
        print(f"{alumno}: ", end="")
        suma = 0
        for nota in alumnos[alumno]:
            suma += nota
        print(suma / 3)
except:
    print("Se ingreso un caracter invalido en una nota")


print("------------------------------------Ejercicio 7------------------------------------")

parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

#Declaro las variables a usar, y asigno algunas a parcial 2 ya que voy a recorrer parcial1
aprueba_dos = []
aprueba_uno = parcial2
alumnos = parcial2

for alumno in parcial1:
    #Si esta en ambos sets lo agrego al aprueba_dos y lo saco del aprueba uno
    if alumno in parcial2:
        aprueba_dos.append(alumno)
        aprueba_uno.remove(alumno)
    #Sino lo agrego al aprueba_uno
    else:
        aprueba_uno.add(alumno)
    #Agrego los alumnos restantes al total de alumnos
    alumnos.add(alumno)

print(f"Aprobaron 2 parciales: {aprueba_dos}")
print(f"Aprobaron 1 parcial: {aprueba_uno}")
print(f"Estudiantes que aprobaron al menos 1 parcial: {alumnos}")

print("------------------------------------Ejercicio 8------------------------------------")

bebidas = {"agua": 20, "coca-cola": 10, "sprite": 8}

#Genero un while con un menú
while True:
    print("MENÚ DE OPCIONES")
    print("1. Consultar stock")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        #Busco el nombre de un producto y si existe muestro sus unidades
        producto = input("Ingresá el nombre del producto: ").lower()
        if producto in bebidas:
            print(f"El stock de {producto} es {bebidas[producto]} unidades.")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")

    elif opcion == "2":
        #Busco un producto, y si existe le agrego las unidades ingresadas
        producto = input("Ingresá el nombre del producto: ").lower()
        if producto in bebidas:
            cantidad = int(input("Ingrese las unidades a agregar: "))
            bebidas[producto] += cantidad
            print("Stock agregado exitosamente.")
        else:
            print(f"El producto '{producto}' no existe.")

    elif opcion == "3":
        #Creo un nuevo producto con sus unidades
        producto = input("Ingresá el nombre del nuevo producto: ").lower()
        if producto in bebidas:
            print("Ese producto ya existe.")
        else:
            cantidad = int(input("Ingrese las unidades que tiene: "))
            bebidas[producto] = cantidad
            print("Producto agregado exitosamente")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")


print("------------------------------------Ejercicio 9------------------------------------")

agenda = {
    ("lunes", "08:00"): "Artitectura en sistemas",
    ("lunes", "10:00"): "Programación",
    ("martes", "08:00"): "Organización Empresarial",
    ("martes", "10:00"): "Matématica",
    ("miércoles", "08:00"): "Programación",
    ("miércoles", "10:00"): "Matématica",
}

print("Consulta a tu agenda")
dia = input("Ingresa el día: ")
hora = input("Ingresa la hora (HH:MM): ")
clave = (dia, hora)

if clave in agenda:
    print(f"A las {hora} del {dia} tenés: {agenda[clave]}")
else:
    print(f"No hay actividad programada el {dia} a las {hora}.")

print("------------------------------------Ejercicio 10------------------------------------")

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

capitales = {}

for pais in paises:
    capitales[paises[pais]] = pais

print(capitales)