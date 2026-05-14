#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  *
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.

#inicio
#obtenemos los datos
#guardar valores de p1 y p2
#recorremos los datos
# si es p1
#  se le suma puntos a p1
#  si tiene 0 p muestra love
# si no es p2
#  se le suma puntos a p2
#  si tiene 0 p muestra love
# muestre los puntos
#si es un empate
# muestra deuce

#despues de los 40 p para ganar debe de ganar 2 p seguimos
#sino no gana


def partido_de_tenis():
    puntuacion = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

    point_p1 = 0
    point_p2 = 0
    marcador = ("Love", "15", "30", "40")

    for p in puntuacion:
        if p == "P1":
            point_p1 += 1
        elif p == "P2":
            point_p2 += 1
        
        if (point_p1 >= 4 or point_p2 >= 4) and abs(point_p1 - point_p2) >= 2 :
                
            if point_p1 > point_p2:
                print("Ganador P1")
            else:
                print("Ganador P2")
            break

        elif point_p1 >= 3 and point_p2 >= 3:

            if point_p1 == point_p2:
                print("Deuce")

            elif abs(point_p1 - point_p2) == 1:
                if point_p1 > point_p2:
                    print("Ventaja P1")
                else:
                    print("Ventaja P2")

        else:
            
            print(marcador[point_p1], "-", marcador[point_p2])


partido_de_tenis()











# def partido_de_tenis():
#     puntuacion = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

#     point_p1 = "Love"
#     point_p2 = "Love"
#     n_p1 = 0
#     n_p2 = 0

#     for p in puntuacion:


#         if point_p1 == "15" or point_p1 == "Love":
#             n_p1 += 15
#             point_p1 = str(n_p1)
#         elif point_p2 == "15" or point_p2 == "Love":
#             n_p2 += 15
#             point_p2 = str(n_p2)
            
#         elif p == "P1":
#             n_p1 += 10
#             point_p1 = str(n_p1)
#         elif p == "P2":
#             n_p2 += 10
#             point_p2 = str(n_p2)

#         print(point_p1, "-", point_p2)

#     if point_p1 == point_p2:
#         print("Deuce")

#     if n_p1 > n_p2:
#         print("Ganador P1")
#         print("Ventaje: P1")
#     elif n_p2 > n_p1:
#         print("Ganador P2")
#         print("Ventaje: P2")

# partido_de_tenis()