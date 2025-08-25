#Se ingresa la fecha
fecha_ingresada = input("Ingrese la fecha con el siguiente formato= día, DD/MM: ")
#Se utiliza un split para separar la fecha en ", "
fecha_separada = fecha_ingresada.split(", ")
#Se obtienen los datos dia, dd y mm
dia = fecha_separada[0].lower()
fecha = fecha_separada[1].split('/')
dd = int(fecha[0])
mm = int(fecha[1])

#Valido si la fecha es existente
if (dd > 31 or mm > 12) or (dia != "lunes" and dia != "martes" and dia != "miercoles" and dia != "jueves" and dia != "viernes"):
    print("Se ingreso una fecha inexistente")
else:
    #Si el día corresponde a uno de los niveles(inicial, intermedio y avanzado)
    if(dia == "lunes" or dia == "martes" or dia == "miercoles"):
        #Se debe ingresar si hubo examen
        examen = input("Ingrese si hubo examen, 'SI' para si y otro caracter para no: ")
        #Si hubo examen
        if(examen == "SI"):
            #Ingreso la cantidad de aprobados y desaprobados
            aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
            desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
            #Se calcula el porcentaje de aprobados
            total_alumnos = aprobados + desaprobados
            porcentaje_aprobados = (total_alumnos * aprobados) / 100
            print(f"Aprobo el {porcentaje_aprobados}%")
        else:
            print("Ese día no se tomaron examenes")
    #Si el día corresponde a las practicas
    elif(dia == "jueves"):
        #Se ingresa la asistencia a clase y se verifica si asistieron o no
        asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
        if(asistencia >= 50):
            print("asistió la mayoria")
        else:
            print("no asistió la mayoria")
    #Si no corresponde a los otros días, corresponde al día de clase para viajeros
    else:
        #Si el día corresponde a un nuevo ciclo
        if(dd == 1 and (mm == 1 or mm == 7)):
            print("Comienzo de nuevo ciclo")
            #Ingreso los nuevos alumnos, el arancel y calculo el ingreso total
            nuevos_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel = float(input("Ingrese el arancel: "))
            ingreso_total = arancel * nuevos_alumnos
            print(f"El ingreso total es de ${ingreso_total}")
        else:
            print("Clase para viajeros")
        










