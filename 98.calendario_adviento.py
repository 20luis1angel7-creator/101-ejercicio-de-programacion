# /*
#  * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
#  * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
#  * Desde el 1 al 24 de diciembre.
#  *
#  * Crea un programa que simule el mecanismo de participación:
#  * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
#  *   participantes, mostrarlos, lanzar el sorteo o salir.
#  * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
#  * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
#  *   (Y no lo duplicarás)
#  * - Si seleccionas mostrar los participantes, se listarán todos.
#  * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
#  *   (Avisando de si lo has eliminado o el nombre no existe)
#  * - Si seleccionas realizar el sorteo, elegirás una persona al azar
#  *   y se eliminará del listado.
#  * - Si seleccionas salir, el programa finalizará.
#  */

import random

def calendario_adviento():
    participantes = []
    seguir = True
    while seguir == True:
        print("1. Añadir participante")
        print("2. Mostrar participantes")
        print("3. Eliminar participante")
        print("4. Realizar sorteo")
        print("5. Salir")
        resp = input(": ")

        if resp == "1":
            resp1 = input("escribe su nombre: ")
            if resp1 in participantes:
                print("ya existe")
            else:
                participantes.append(resp1)

        elif resp == "2":
            print(participantes)

        elif resp == "3":
            resp1 = input("cual nombre eliminar: ")
            if resp1 not in participantes:
                print("no esta en la lista")
            else:
                participantes.remove(resp1)
            print(participantes)
        
        elif resp == "4":
            sorteo = True
            resp = "si"
            while sorteo == True:
                if participantes:
                    if resp == "si":

                        rendom = random.choice(participantes)
                        participantes.remove(rendom)
                        print(rendom)
                        sorteo = True
                    elif resp == "no":
                        sorteo = False
                    resp = input("seguir: ")
                else:
                    print("no hay participantes")
                    sorteo = False

        elif resp == "5":
            seguir = False
            

    
calendario_adviento()