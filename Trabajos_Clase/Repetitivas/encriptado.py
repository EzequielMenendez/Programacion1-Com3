#constante con las letras de abecedario
ABECEDARIO = "abcdefghijklmñnopqrstuvwxyz"
#se pide ingresar el corrimiento del mensaje
corrimiento = int(input("Ingrese el corrimiento del mensaje: "))
#Se usa un for para recorrer 5 veces
for oficial in range(1, 6):
    #Se ingresa en mensaje a encriptar
    mensaje = input("Ingrese el mensaje a enviar: ").lower()
    encriptado = ""
    #Para cada letra en el mensaje
    for letra in mensaje:
        #Valido si la letra esta en el abecedario
        if letra in ABECEDARIO:
            #calculo el indice del abecedario + el corriemiento
            indice = (ABECEDARIO.index(letra) + corrimiento) % 27
            #Guardo la letra en el abecedario
            encriptado += ABECEDARIO[indice]
        else:
            #si no esta en el abecedario, lo guardo normalmente
            encriptado += letra
    print(f"Oficial {oficial}, Mensaje: {encriptado}")