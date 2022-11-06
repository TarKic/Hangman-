import random

def buscaPalabras (): #Cargamos un archivos con palabras y acá, la traemos al programa principal como lista
    try:
        arch = open ("palabras.txt", "rt")
    except IOError:
        print ("No se pudo abrir el archivo...")
    else:
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
    archivo.write (nombre  + " utilizo " + puntos + " intentos" + '\n')
    archivo.close()



cantidadDeJugadores = int (input ("Ingrese la cantidad de usuarios que jugaran: "))
yaJugaron = 0

while (yaJugaron < cantidadDeJugadores ):
    nombre = input ("Ingrese el nombre de la persona que jugara: ")
   
    yaJugaron += 1 #Sumador para indicar que un jugador comenzó un nuevo juego
    #Llamado a las funciones requeridas para el funcionamiento del programa
    lista = buscaPalabras ()
    palabra = seleccionaPalabra (lista)
    tablero = generaRenglones (palabra)
    chances = 6
    intentos = 0
    print (palabra) #La dejo para ir probando si funciona el codigo, pero hay que sacar este print
    cantidadLetras = len(palabra) - 1
    while (chances > intentos): #Mientras no llegue a los 5 intentos, sigue pidiendole letras y llena el tablero (los rengoles) con las letras correctas que el usuario va poniendo
        esta = False 
        termino = False
        palabraAdivinada = ''.join (tablero) #pasa a string la lista tablero para que quede como palabra 
        print (palabraAdivinada) 
        letra = input ("Ingrese la letra: ")
        for i in range (len(palabra)-1):
            if (palabra[i] == letra):
                tablero[i] = letra
                esta = True
        if (esta == True):
            print ("Acertaste!")
        


        
        if (esta == False): #Aca esta el sumador de intentos
            intentos += 1
            restantes = chances - intentos 
            dibujo = dibujaPersona (intentos)
            print ("Te quedan", restantes,'intentos')
      
    


    datos = (nombre,intentos)
    archivoPuntos = generaArchivoPuntuacion (datos)
    if (restantes == 0 or intentos == 6):
        print ("Perdiste... La palabra era", palabra) #Mensaje si el usuario pasa los intentos sin poder adivinar la palabra
    