# /*
#  * Crea un juego interactivo por terminal en el que tendrás que adivinar
#  * el resultado de diferentes operaciones matemáticas aleatorias
#  * (suma, resta, multiplicación o división de dos números enteros).
#  * - Tendrás 3 segundos para responder correctamente.
#  * - El juego finaliza si no se logra responder en ese tiempo.
#  * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
#  * - Cada 5 aciertos debes aumentar en uno el posible número de cifras
#  *   de la operación (cada vez en un operando):
#  *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
#  *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
#  *   - Preguntas 11 a 15: XX operación YY
#  *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
#  *   ..
#  */

#inicio
#mostrar operacion mat
#si la puntuacion es menor o igual que 5:
# numeros random del 0 al 9
#si la puntuacion es mayor que 6 y menos que 10:
# numeros random del 0 al 99
#si la puntuacion es menor 11 y mayor que 15:
# num
#si la puntuacion es menor 16 y mayor que 20:
# num random 0 al 999
#crear varias operaciones (cambian los numeros) y que sea areatoria
#input
#comparar el resultado si son iguales seguimos (while)
#se aumenta un punto

import random
import threading
import queue

def adivinanzas_mat():
    puntuacion = 0

    while True:
        
        resp = operaciones(puntuacion)

        
        if not resp:
            
            print("juego terminado! haz acertado ", puntuacion)
            break
        
        puntuacion += 1


def operaciones(puntuacion):
    nivel = puntuacion // 5

    limite1 = (10 ** (nivel + 1)) - 1
    limite2 = (10 ** nivel) - 1

    num1 = random.randint(0, limite1)
    num2 = random.randint(0, limite2)

    # if puntuacion < 5:
    #     num1 = random.randint(0, 9)
    #     num2 = random.randint(0, 9)
    # elif puntuacion < 10:
    #     num1 = random.randint(0, 99)
    #     num2 = random.randint(0, 9)
    # elif puntuacion < 15:
    #     num1 = random.randint(0, 99)
    #     num2 = random.randint(0, 99)
    # elif puntuacion < 20:
    #     num1 = random.randint(0, 999)
    #     num2 = random.randint(0, 99)
    # elif puntuacion < 25:
    #     num1 = random.randint(0, 999)
    #     num2 = random.randint(0, 999)
    # elif puntuacion >= 25:
    #     print("terminaste")
        

    operaciones = random.choice(["+", "-", "*","/"])
    if operaciones == "+":
        result = num1 + num2
    elif operaciones == "-":
        result = num1 - num2
    elif operaciones == "*":
        result = num1 * num2
    elif operaciones == "/":
        while num2 == 0 or num1 % num2 != 0:
            num1 = random.randint(0, limite1)
            num2 = random.randint(1, limite2)
        
        result = num1 // num2
    else:
        print("....")


    # res = float(result)
    # print(res)
    print(f"{num1} {operaciones} {num2} = ")

    respuestas = queue.Queue()

    def pedir_respuesta():
        try:
            respuesta = input("tu respuesta: ")
            respuestas.put(respuesta)

        except EOFError:
            respuestas.put(None)

    try:
        respuesta_usuario = respuestas.get(timeout=5)

        if respuesta_usuario is None:
            return False

        respuesta_usuario = float(respuesta_usuario)

    except queue.Empty:
        print("se acabo el tiempo")
        return False

    except ValueError:
        print("introduce numero valido")
        return False
        
    if respuesta_usuario == result:
        return True
    else:
        print(f"❌ Respuesta incorrecta. No puedes avanzar. el resultado era {result}")
        return False


adivinanzas_mat()



























# . ➕ Sumas

#     245 + 132 = 377
#     368 + 217 = 585
#     456 + 329 = 785
#     527 + 184 = 711
#     643 + 258 = 901

# 2. ➖ Restas

#     458 − 236 = 222
#     675 − 342 = 333
#     824 − 417 = 407
#     936 − 528 = 408
#     700 − 265 = 435

# 3. ✖️ Multiplicaciones

#     24 × 3 = 72
#     36 × 5 = 180
#     47 × 6 = 282
#     125 × 4 = 500
#     238 × 7 = 1,666

# 4. ➗ Divisiones

#     48 ÷ 6 = 8
#     72 ÷ 8 = 9
#     96 ÷ 4 = 24
#     144 ÷ 12 = 12
#     225 ÷ 5 = 45
