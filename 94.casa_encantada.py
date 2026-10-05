# /*
#  * Este es un reto especial por Halloween.
#  * Te encuentras explorando una mansión abandonada llena de habitaciones.
#  * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
#  * Tu misión es encontrar la habitación de los dulces.
#  *
#  * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
#  * (Tienes total libertad para ser creativo con los textos)
#  *
#  * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
#  *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
#  *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
#  *   Esta podría ser una representación:
#  *   🚪⬜️⬜️⬜️
#  *   ⬜️👻⬜️⬜️
#  *   ⬜️⬜️⬜️👻
#  *   ⬜️⬜️🍭⬜️
#  * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
#  *   Si no lo aciertas no podrás desplazarte.
#  * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
#  *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
#  * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
#  * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
#  *   tengas que responder dos preguntas para salir de ella.
#  */

# Fase 1
# Haz solamente:
# 🚪⬜⬜⬜
# ⬜⬜⬜⬜
# ⬜⬜⬜⬜
# ⬜⬜🍭⬜
# y consigue que el jugador tenga una posición.

# Fase 2
# Haz que pueda moverse:
# Norte
# Sur
# Este
# Oeste
# pero únicamente cuando el movimiento sea válido.

# Fase 3
# Añade los acertijos.
# Pregunta:
# ¿Qué tiene agujas pero no cose?
# Respuesta:
# reloj

# Fase 4
# Haz que las preguntas sean aleatorias.

# Fase 5
# Añade los fantasmas.
# 👻
# Pregunta 1 → correcta
# Pregunta 2 → correcta
# Puedes continuar.

# Fase 6
# Añade la condición de victoria:
# 🍭
# ¡Has encontrado los dulces!
# ¡Has escapado de la mansión! 🎃

import random

def cuadrilla(c, f):
    cuadricula = [["⬜" for _ in range(c)] for _ in range(f)]
    fantasmas = [["⬜" for _ in range(c)] for _ in range(f)]

    fila = 0
    columna = 0

    cuadricula[0][0] = "🚪"
    cuadricula[3][2] = "🍭"
    
    while cuadricula[fila][columna] != "🍭":

        for i in range(f):
            for j in range(c):
                if i == fila and j == columna:
                    print("🧙", end=" ")
                elif fantasmas[i][j] == "👻":
                    print("👻", end=" ")
                else:
                    print(cuadricula[i][j], end=" ")
            print()

        mov = input("donde quieres ir? ")

        if 0 <= columna < c and 0 <= fila < f:
            if mov == "d" and columna < c - 1:
                columna += 1
                acertijo()
                if fantasma():
                    fantasmas[fila][columna] = "👻"
            elif mov == "a" and columna > 0:
                if acertijo():
                    columna -= 1
                    if fantasma():
                        fantasmas[fila][columna] = "👻"
            elif mov == "s" and fila < f - 1:
                if acertijo():
                    fila += 1
                    if fantasma():
                        fantasmas[fila][columna] = "👻"
            elif mov == "w" and fila > 0:
                if acertijo():
                    fila -= 1
                    if fantasma():
                        fantasmas[fila][columna] = "👻"
            else:
                print("solo se puede: s, a, d, w ")
        else: 
            print("te saliste de las casillas")
        
    
def acertijo():
    acertijos = [
                ["¿Qué tiene agujas pero no cose?", "reloj"],
                ["¿Qué tiene dientes pero no puede comer?", "peine"],
                ["¿Qué tiene cuello pero no cabeza?", "botella"],
                ["¿Qué tiene hojas pero no es un árbol?", "libro"],
                ["¿Qué tiene manos pero no puede aplaudir?", "reloj"],
                ["¿Qué tiene un ojo pero no puede ver?", "aguja"],
                ["¿Qué sube y baja pero siempre está en el mismo lugar?", "escalera"],
                ["¿Qué tiene patas pero no puede caminar?", "mesa"],
                ["¿Qué se moja mientras seca?", "toalla"],
                ["¿Qué tiene ciudades, pero no casas; tiene montañas, pero no árboles?", "mapa"],
                ["¿Qué cuanto más le quitas, más grande se vuelve?", "agujero"],
                ["¿Qué tiene cabeza y cola, pero no tiene cuerpo?", "moneda"],
                ["¿Qué corre pero no tiene piernas?", "agua"],
                ["¿Qué tiene teclas pero no puede abrir ninguna puerta?", "piano"],
                ["¿Qué puede viajar por todo el mundo sin moverse de una esquina?", "sello"],
                ["¿Qué tiene alas pero no puede volar?", "molino"],
                ["¿Qué tiene una cara y dos manos, pero no tiene brazos?", "reloj"],
                ["¿Qué desaparece en cuanto dices su nombre?", "silencio"],
                ["¿Qué tiene muchos agujeros pero puede contener agua?", "esponja"],
                ["¿Qué entra al agua pero nunca se moja?", "sombra"]
            ]
    aleatorio = random.choice(acertijos)
    preg = aleatorio[0]
    resp = aleatorio[1]
    print(preg)

    resp_usuario = input("Respuesta: ")

    if resp_usuario.lower() == resp:
        return True
    else:
        print("❌ Respuesta incorrecta. No puedes avanzar.")
        return False
    


def fantasma():
    numero_rando = random.randint(1, 100)

    if numero_rando <= 10:
        
        return True
    else:
        return False


cuadrilla(4, 4)




