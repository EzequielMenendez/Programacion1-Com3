import random
#Constante de opciones del juego
OPCIONES = {1: "Piedra", 2: "Papel", 3: "Tijera"}
#Defino los contadores
contador_pc = 0
contador_jugador = 0
#Ejecuto un mientras para empezar un bucle
while True:
    #La computadora obtiene una elección random
    numero_pc = random.randint(1, 3)
    #El jugador hace su elección
    numero_jugador = int(input("Elige 1 para piedra, 2 para papel y 3 para tijera: "))
    #Si ambas elecciones son iguales, entonces hay empate
    if numero_jugador == numero_pc:
        print("Empate")
    #Evaluo las condiciones donde el jugador gana
    elif (numero_jugador == 1 and numero_pc == 3) or (numero_jugador == 2 and numero_pc == 1) or (numero_jugador == 3 and numero_pc == 2):
        #En caso de ganar, muesto el mensaje y sumo 1 punto al contandor del jugador
        print(f"{OPCIONES[numero_jugador]} gana a {OPCIONES[numero_pc]}")
        contador_jugador += 1
    #Si no, es por que el jugador perdio
    else:
        #Por lo que muestro el mensaje de derrota y sumo 1 punto al contador de la computadora
        print(f"{OPCIONES[numero_jugador]} pierde contra {OPCIONES[numero_pc]}")
        contador_pc += 1
    #Muestro un mensaje de los resultados del jugador contra la computadora
    print(f"Jugador: {contador_jugador} VS Computadora: {contador_pc}")
    #Le pido al usuario si desea continuar
    continuar = input("Desea continuar jugando? Presione 'S' para continuar, y cualquier otra tecla para salir: ").upper()
    #En caso de que no desee continuar rompo el bucle
    if continuar != "S":
        break