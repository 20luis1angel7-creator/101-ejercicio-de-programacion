#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
#  *   o "S" (tijera).
#  * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 

#inicio
#ingresar lista
#lo separamos (para que queden 2, ej: ("R","S"))
#si j1 tiene piedra y j2 tiene tijera or j1 tiene tijera y j2 tiene papel or j1 tiene papel y j2 tiene piedra
#se le suma 1 punto a j1
#lo mismo con el j2 pero al reves
#mostrar el ganador o empate


juego = [("R","S"), ("S","R"), ("P","S")]
def game(juego):
    try:
        reglas = {
            "R":"S",
            "P":"R",
            "S":"P"
        }

        puntoj1 =0
        puntoj2 =0

        for j1, j2 in juego:

            if j1 == j2:
                continue

            if reglas[j1] == j2:
                puntoj1 += 1
            else:
                puntoj2 += 1
            
        print("winer")
        if puntoj1 > puntoj2:
            return "Player 1"
        elif puntoj1 < puntoj2:
            return "Player 2"
        else:
            return "Tie"
    except ValueError:
        return "error"

print(game(juego))


# def game():
#     juego = [("R","S"), ("S","R"), ("P","S")]
#     puntoj1=0
#     puntoj2=0

#     for j1, j2 in juego:
#         if j1 == "R" and j2 == "S":
#             puntoj1 += 1
#         elif j1 == "S" and j2 == "R":
#             puntoj2 += 1

#         if j1 == "P" and j2 == "R":
#             puntoj1 += 1
#         elif j1 == "R" and j2 == "P":
#             puntoj2 += 1

#         if j1 == "S" and j2 == "P" :
#             puntoj1 += 1
#         elif j1 == "P" and j2 == "S":
#             puntoj2 += 1


#     print("winer")
#     if puntoj1 > puntoj2:
#         print("Player 1")
#     elif puntoj1 < puntoj2:
#         print("Player 2")
#     else:
#         print("Tie")

# game()



