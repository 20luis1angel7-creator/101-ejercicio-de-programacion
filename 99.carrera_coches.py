#  * Crea un programa que simule la competición de dos coches en una pista.
#  * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
#  * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
#  * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
#  * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
#  *   🏁____🌲_____🚙
#  *   🏁_🌲____🌲___🚗
#  *
#  * El juego se desarrolla por turnos de forma automática, y cada segundo
#  * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
#  * uno de ellos (o los dos a la vez) llega a la meta.
#  * - Acciones:
#  *   - Avanzar entre 1 a 3 posiciones hacia la meta.
#  *   - Si al avanzar, el coche finaliza en la posición de un árbol,
#  *     se muestra 💥 y no avanza durante un turno.
#  *   - Cada turno se imprimen las pistas y sus elementos.
#  *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
#  */




import random
import time

def carrera_de_coches():
    choque_coche1 = False
    choque_coche2 = False

    pista1 = ["_"] * 20
    pista2 = ["_"] * 20

    posicion_coche1 = 19
    posicion_coche2 = 19

    coche1 = "🚙"
    coche2 = "🚗"

    cant_arbol = num_random(1, 3)
    arboles_pista1 = []
    arboles_pista2 = []

    for i in range(cant_arbol):

        num1 = num_random(1, 18)
        num2 = num_random(1, 18)

        while num1 in arboles_pista1:
            num1 = num_random(1, 18)

        while num2 in arboles_pista2:
            num2 = num_random(1, 18)

        arboles_pista1.append(num1)
        arboles_pista2.append(num2)

    for posicion in arboles_pista1:
        pista1[posicion] = "🌲"

    for posicion in arboles_pista2:
        pista2[posicion] = "🌲"

    while posicion_coche1 != 0 or posicion_coche2 != 0:

        # Movimiento del coche 1
        if posicion_coche1 != 0:

            if choque_coche1:
                print("🚙 Pierde un turno")
                choque_coche1 = False

            else:
                mov1 = num_random(1, 3)
                nueva_posicion1 = max(0, posicion_coche1 - mov1)

                if nueva_posicion1 in arboles_pista1:
                    print("💥 Choque coche 1")
                    choque_coche1 = True
                else:
                    posicion_coche1 = nueva_posicion1

        # Movimiento del coche 2
        if posicion_coche2 != 0:

            if choque_coche2:
                print("🚗 Pierde un turno")
                choque_coche2 = False

            else:
                mov2 = num_random(1, 3)
                nueva_posicion2 = max(0, posicion_coche2 - mov2)

                if nueva_posicion2 in arboles_pista2:
                    print("💥 Choque coche 2")
                    choque_coche2 = True
                else:
                    posicion_coche2 = nueva_posicion2

        # Reconstruir las pistas
        pista1 = ["_"] * 20
        pista2 = ["_"] * 20

        for posicion in arboles_pista1:
            pista1[posicion] = "🌲"

        for posicion in arboles_pista2:
            pista2[posicion] = "🌲"

        pista1[posicion_coche1] = coche1
        pista2[posicion_coche2] = coche2

        # Imprimir las pistas
        print("\n🏁 TURNO")
        print("".join(pista1))
        print("".join(pista2))

        time.sleep(1)

    # Resultado de la carrera
    print("\n🏁 FIN DE LA CARRERA")

    if posicion_coche1 == 0 and posicion_coche2 == 0:
        print("¡EMPATE!")
    elif posicion_coche1 == 0:
        print("¡GANÓ 🚙!")
    else:
        print("¡GANÓ 🚗!")


def num_random(n1, n2):
    num_avanzar = random.randint(n1, n2)
    return num_avanzar


carrera_de_coches()


# import random
# def carrera_de_coches():
#     choque_coche1 = False
#     choque_coche2 = False

#     pista1 = ["_"] * 20
#     pista2 = ["_"] * 20

#     posicion_coche1 = 19
#     posicion_coche2 = 19

#     coche1 = "🚙"
#     coche2 = "🚗"

#     cant_arbol = num_random(1, 3)
#     arboles_pista1 = []
#     arboles_pista2 = []

#     for i in range(cant_arbol):
#         num1 = num_random(0, 19)
#         num2 = num_random(0, 19)

#         if num1 not in arboles_pista1:
#             arboles_pista1.append(num1)
#         if num2 not in arboles_pista2:
#             arboles_pista2.append(num2)
#         print(arboles_pista1)
#         print(arboles_pista2)

#     for posicion in arboles_pista1:        
#         pista1[posicion] = "🌲"
#     for posicion in arboles_pista2:            
#         pista2[posicion] = "🌲"

#     while posicion_coche1 != 0 or posicion_coche2 != 0:
#         mov1 = num_random(1, 3)
#         mov2 = num_random(1, 3)
#         nueva_posicion1 = posicion_coche1 - mov1
#         nueva_posicion2 = posicion_coche2 - mov2

#         if nueva_posicion1 in arboles_pista1:
#                     print("hay un arbol 1")
#                     choque_coche1 = True
#         else:
#             posicion_coche1 = max(0, nueva_posicion1)
        
#         if nueva_posicion2 in arboles_pista2:
#                     print("hay un arbol 2")
#                     choque_coche2 = True
#         else:
#             posicion_coche2 = max(0, nueva_posicion2)

#         print(posicion_coche1)
#         print(posicion_coche2)

# def num_random(n1, n2):
#     num_avanzar = random.randint(n1, n2)
#     return num_avanzar

# carrera_de_coches()


