import random
"""Creo que para el TP usamos archivos, y lo que fuimos viendo antes del primer parcial, no sé como incluiría tuplas, o diccionarios. Tuplas, podemos incluirlo como que el usuario ingrese su nombre y si adivina guardamos en una tupla el nombre del usuario y la cant de intentos, y después, comparamos todos los usuarios y vemos quien lo hizo en menos intentos
x ejemplo (juan, 5) lo comparamos con (gabriel, 2). Lo haria de dos niveles, el nivel facil, que te de la primer letra de la palabra elegida y mas chances , y el avanzado que no te de ninugna pista y tengas menos intentos """


def buscaPalabras (): #Cargamos un archivos con palabras y acá, la traemos al programa principal como lista
    arch = open ("palabras.txt", "rt")
    palabras = arch.readlines ()
    arch.close ()
    return palabras

def generaRenglones (a): #Genera la cantidad de _ que tiene la palabra, simplemente un detalle estético
    lista = []
    for i in range (len(a)-1):
        lista.append ("_") 
    return lista

def seleccionaPalabra (listaImportada): #Busca, aleatoriamente la palabra que será utilizada para que el usuario la adivine
    palabraAdivinar = listaImportada[random.randint(0,len(lista) - 1)] 
    return palabraAdivinar

def dibujaPersona (intentos): # Para dibujar la persona del ahorcado 
    if intentos == 1:
         print("   _____ \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif (intentos == 2):
        print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif (intentos == 3):
         print("   _____ \n"
                 "  |     | \n"
                 "  |     O \n"
                 "  |     |\ \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
    elif (intentos == 4):
        print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif (intentos == 5):
        print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \ \n"
                  "__|__\n")
    elif (intentos == 6):
        print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"    
                  "  |        \n"
                  "  |         \n"
                  "__|__\n")
   
def generaArchivoPuntuacion (tupla):
    archivo = open ("puntuaciones.txt",'wt')
    nombre,puntos = tupla
    puntos = str(puntos)
    archivo.write (nombre + puntos + '\n')
    archivo.close()



cantidadDeJugadores = int (input ("Ingrese la cantidad de usuarios que jugaran: "))
yaJugaron = 0
while (yaJugaron < cantidadDeJugadores):
    yaJugaron += 1
    lista = buscaPalabras ()
    palabra = seleccionaPalabra (lista)
    tablero = generaRenglones (palabra)
    chances = 6
    intentos = 0
    print (palabra) #La dejo para ir probando si funciona el codigo, pero hay que sacar este print

    nombre = input ("Ingrese el nombre de la persona que jugara: ")

    while (chances > intentos): #Mientras no llegue a los 5 intentos, sigue pidiendole letras y llena el tablero (los rengoles) con las letras correctas que el usuario va poniendo
        esta = False 
        termino = False
        print (tablero) 
        letra = input ("Ingrese la letra: ")
        for i in range (len(palabra)-1):
            if (palabra[i] == letra):
                print ("Acertaste...")
                tablero[i] = letra
                print (tablero)
                esta = True
            palabraAdivinada = ''.join (tablero) #pasa a string la lista tablero para que quede como palabra 
        print (palabra)

        print (palabraAdivinada)
        for i in range (len(palabra)):
            if palabra.lower() == palabraAdivinada.lower():
                print ("Adivinaste!")
                intentos = 6
            
   
        
        if (esta == False): #Aca esta el sumador de intentos
            intentos += 1
            restantes = chances - intentos 
            dibujo = dibujaPersona (intentos)
            print ("Te quedan", restantes,'intentos')

    datos = (nombre,intentos)

    print ("Perdiste... La palabra era", palabra) #Mensaje si el usuario pasa los intentos sin poder adivinar la palabra