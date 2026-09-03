#  * Crea un programa capaz de interactuar con un fichero TXT.
#  * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección.
#  * Únicamente el código.
#  *
#  * - Si no existe, debe crear un fichero llamado "text.txt".
#  * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
#  *   en una nueva línea cada vez que se pulse el botón "Enter".
#  * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
#  *   a continuación o borrar su contenido y comenzar desde el principio.
#  * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
#  *   el texto que ya posee el fichero. 
#  */



# estudio
# 1. Archivos / ficheros

# Aprende qué es un fichero y cómo un programa puede:

#     Crear un fichero.
#     Abrir un fichero.
#     Leer un fichero.
#     Escribir en un fichero.
#     Añadir información al final.
#     Cerrar un fichero.

# 3. Modos de apertura de archivos

# Especialmente:

#     Lectura
#     Escritura
#     Añadir

# Y tienes que entender muy bien la diferencia entre escribir reemplazando y añadir al final.

# 4. Entrada por consola

# Necesitas saber cómo:

#     Mostrar un mensaje al usuario.
#     Leer lo que escribe.
#     Detectar que ha pulsado Enter.

# El ejercicio depende bastante de esto porque vas a recibir texto continuamente.

# 7. Cadenas de texto

# También te conviene saber trabajar con String/cadenas, porque vas a recibir texto del usuario y tendrás que comprobar posiblemente qué opción ha elegido.

import os

def fichero():
    # with open("text.txt", "w") as archivo:
    #     archivo.write("hola\n")

    # with open("text.txt", "r") as arc:
    #     contenido = arc.read()
    # print(contenido)

    # with open("text.txt", "a") as arch:
    #     arch.write("como estas?\n")
    
    exist = os.path.exists("text.txt")

    if exist is False:
        with open("text.txt", "w") as archivo:
            while True:
                texto = input()

                if texto == "":
                    break

                contenido = archivo.write(texto + "\n")

    elif exist:
        opcion = input("continuar escribiendo o borrar el contenido? ")

        if opcion == "continuar":
            with open("text.txt", "r") as archivo:
                contenido = archivo.read()
            print(contenido)

            while True:
                texto = input()
                # print(repr(texto))

                if texto == "":
                    break

                with open("text.txt", "a") as archivo:
                    archivo.write(texto + "\n")
                    
        elif opcion == "borrar":
            
            with open("text.txt", "w") as archivo:
                while True:
                    texto = input()

                    if texto == "":
                        break

                    contenido = archivo.write(texto + "\n")
fichero()