#  * La última semana de 2021 comenzamos la actividad de retos de programación,
#  * con la intención de resolver un ejercicio cada semana para mejorar
#  * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
#  *
#  * Crea un programa que calcule los puntos de una palabra.
#  * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
#  *   español de 27 letras, la A vale 1 y la Z 27.
#  * - El programa muestra el valor de los puntos de cada palabra introducida.
#  * - El programa finaliza si logras introducir una palabra de 100 puntos.
#  * - Puedes usar la terminal para interactuar con el usuario y solicitarle
#  *   cada palabra.
#  */


#inicio
#declarar el valor de cada letra
#insertar una palabra
#descomprimir a letras
#ir letra por letra buscando su numero
#   ir sumandola y guardarla
#mostrar


def palabra_100():
    letras = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
    }
    
    puntos = True
    
    while puntos:
        sum_datos = 0
        palabra_insertada = input("tu palabra: ")

        for i in palabra_insertada:
            print(i)
            if i == " ":
                print("no se acepta espacio")
                break

            if i in letras:
                datos = letras.get(i)
                sum_datos += datos
                print(datos)
                print(sum_datos)
            
        if sum_datos == 100:
            puntos = False
            print("felicidades! Legaste a 100 puntos")

palabra_100()