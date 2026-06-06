#  * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  *   la palabra a adivinar)
#  *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  *   - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
#  *   ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres


#inicio
#palabra
#mostrar palabra ocultando el 60%
#un while si no toene 0 vidas
# ingresar palabra
# si falla restar vida
# si acerto retornar la palabra
#fin

import random 

def adivina_palabra():
    word = "mauredev"

    visible = round(len(word) * 0.6)

    letter = set(random.sample(range(len(word)), visible))

    result = ""

    for i, value in enumerate(word):
        if i in letter:
            result += value
        else:
            result += "_"

    print(result)
adivina_palabra()