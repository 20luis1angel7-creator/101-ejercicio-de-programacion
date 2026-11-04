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
        print("correcto! puntuacion: ", puntuacion)

def operaciones(puntuacion):
    nivel = puntuacion // 5

    limite1 = (10 ** (nivel + 1)) - 1
    limite2 = (10 ** (nivel + 1)) - 1 if nivel % 2 == 0 else ( 10 ** nivel) - 1

    num1 = random.randint(0, limite1)
    num2 = random.randint(0, limite2)     

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
            num2 = random.randint(1, max( 1, limite2))
        
        result = num1 // num2
    
    print(f"{num1} {operaciones} {num2} = ")

    respuestas = queue.Queue()

    def pedir_respuesta():
        try:
            respuesta = input("tu respuesta: ")
            respuestas.put(respuesta)

        except EOFError:
            respuestas.put(None)

    hilo = threading.Thread(target=pedir_respuesta)
    hilo.daemon = True
    hilo.start()

    try:
        respuesta_usuario = respuestas.get(timeout=10)

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









