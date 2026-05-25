#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.


#inicio
#obtener las combinaciones
#variable de puntos
#separo la partes
#lo comparo cada uno ("🗿","✂️")
#sumamos los puntos
#mostramo quien gano 
#o si fue un empate

reglas = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️"), ("🦎","🖖"), ("🖖","🗿")]

def PPTLS(reglas):
    posicion = {
        "🗿": "🦎",
        "🗿": "✂️",
        "🦎": "📄",
        "🦎": "🖖",
        "✂️": "🦎",
        "✂️": "📄",
        "🖖": "✂️",
        "🖖": "🗿",
        "📄": "🖖",
        "📄": "🗿",
    }
    jugador_1 = 0
    jugador_2 = 0

    for j1, j2 in reglas:
        if posicion[j1] == j2:
            jugador_1 += 1
        else:
            jugador_2 += 1
        
    #print(jugador_1, jugador_2)
    if jugador_1 == jugador_2:
        print("Tie")
    elif jugador_1 > jugador_2:
        print("Ganador es el jugador 1:", jugador_1, "a", jugador_2, "puntos")
    elif jugador_2 > jugador_1:
        print("Ganador es el jugador 2:", jugador_2, "a", jugador_1, "puntos")
    else:
        print("error")

PPTLS(reglas)