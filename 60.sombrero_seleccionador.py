#  * Crea un programa que simule el comportamiento del sombrero selccionador del
#  * universo mágico de Harry Potter.
#  * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#  * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#  * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  *   coloque al alumno en una de las 4 casas de Hogwarts:
#  *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#  * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
#  *   y crear el algoritmo seleccionador:
#  *   Por ejemplo, en Slytherin se premia la ambición y la astucia.

#inicio
#declara puntos en 0
#preg 1
#mostrar respuesta
#ingresar un numero de respuesta
#sumar y casas
#mostrar la casa

def sombrero_seleccionador():
    pregunt = [
        ("con cual te identificas mas?", "1. Valentia.", "2. Inteligencia.", "3. Ambicion.", "4. Lealtad"),
        ("con cual te identificas mas?", "1. Liderazgo.", "2. Creatividad.", "3. Astucia.", "4. Trabajo duro"),
        ("con cual te identificas mas?", "1. Acción.", "2. Curiosidad.", "3. Estrategia.", "4. Honestidad"),
        ("con cual te identificas mas?", "1. Coraje.", "2. Sabiduría.", "3. Poder.", "4. Amabilidad"),
        ("con cual te identificas mas?", "1. pelear.", "2. telepatico.", "3. hill.", "4. palomo")
    ]
    point_1 = 0
    point_2 = 0
    point_3 = 0
    point_4 = 0

    for preg, res1, res2, res3, res4 in pregunt:
        print(preg)
        print(res1)
        print(res2)
        print(res3)
        print(res4)
        respuesta = input()

        if respuesta == "1":
            point_1 += 1
        elif respuesta == "2":
            point_2 += 1
        elif respuesta == "3":
            point_3 += 1
        elif respuesta == "4":
            point_4 += 1

    puntos = [point_1, point_2, point_3, point_4]
    casas = [ "Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]

    ganador = puntos.index(max(puntos))

    print("Tu casa de Hogwarts es", casas[ganador])

sombrero_seleccionador()

