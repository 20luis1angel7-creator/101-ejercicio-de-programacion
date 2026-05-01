#  * Calcula dónde estará un robot (sus coordenadas finales) que se
#  * encuentra en una cuadrícula representada por los ejes "x" e "y".
#  * - El robot comienza en la coordenada (0, 0).
#  * - Para idicarle que se mueva, le enviamos un array formado por enteros
#  *   (positivos o negativos) que indican la secuencia de pasos a dar.
#  * - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene,
#  *   luego 5, se detiene, y finalmente 2.
#  *   El resultado en este caso sería (x: -5, y: 12)
#  * - Si el número de pasos es negativo, se desplazaría en sentido contrario al
#  *   que está mirando.
#  * - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando
#  *   hacia la parte positiva del eje "y".
#  * - El robot tiene un fallo en su programación: cada vez que finaliza una
#  *   secuencia de pasos gira 90 grados en el sentido contrario a las agujas
#  *   del reloj.




def donde_esta_robot(num_array):
    x = 0
    y = 0
    posicion = ["+y", "-x", "-y", "+x"]
    
    for i, valor in enumerate(num_array):
        direccion = posicion[i % 4]
        print(direccion)
        print(valor)

        if direccion[1] == "x":
            if direccion[0] == "+":
                x += valor
            else:
                x -= valor
        else:
            if direccion[0] == "+":
                y += valor
            else:
                y -= valor

    return x, y

print(donde_esta_robot([10, 5,-2,-12, 10]))



# def donde_esta_el_robot(array):
#     y = 0
#     x = 0
#     mirando = "y+"
#     for i in array:
#         if mirando == "y+" :#and i > 0:
#             y += i
#         # elif mirando == "y+" and i < 0:
#         #     y -= i
            
#         elif mirando == "x-":# and i < 0:
#             x -= i
#         # elif mirando == "x-" and i > 0:
#         #     x -= i
        
#         elif mirando == "y-" :#and i < 0:
#             y -= i
#         # elif mirando == "y-": and i > 0:
#         #     y -= i

#         elif mirando == "x+":# and i > 0:
#             x += i
#         # elif mirando == "x+" and i < 0:
#         #     x -= i

        
#         result = "x:", x, "y:", y
#         print(result)
        

#         if mirando == "y+" and i > 0:
#             mirando = "x-"
#         elif mirando == "y+" and i < 0:
#             mirando = "x+"

#         elif mirando == "x-" and i > 0:
#             mirando = "y-"
#         elif mirando == "x-" and i < 0:
#             mirando = "y+"

#         elif mirando == "y-" and i > 0:
#             mirando = "x+"
#         elif mirando == "y-" and i < 0:
#             mirando = "x-"

#         elif mirando == "x+" and i > 0:
#             mirando = "y+"
#         elif mirando == "x+" and i < 0:
#             mirando = "y-"

#     return result
        

# print(donde_esta_el_robot([10, 5,-2,-12,10]))



# def donde_esta_el_robot(array):
#     coordenada = (0, 0)
#     y = 0
#     x = 0
#     mirando = "y+"
#     for i in array:
#         if mirando == "y+":
#             y += i
            
#         elif mirando == "x-":
#             x -= i
        
#         elif mirando == "y-":
#             y -= i

#         elif mirando == "x+":
#             x += i

        
#         resutl = "x:", x, "y:", y
        

#         direcciones = "y+", "x+", "y-", "x-"
#         if mirando == "y+" and i > 0:
#             mirando = "x-"
#         elif mirando == "y+" and i < 0:
#             mirando = "x+"

#         elif mirando == "x-" and i > 0:
#             mirando = "y-"
#         elif mirando == "x-" and i < 0:
#             mirando = "y+"

#         elif mirando == "y-" and i > 0:
#             mirando = "x+"
#         elif mirando == "y-" and i < 0:
#             mirando = "x-"

#         elif mirando == "x+" and i > 0:
#             mirando = "y+"
#         elif mirando == "x+" and i < 0:
#             mirando = "y-"

#     return resutl
        

# print(donde_esta_el_robot([10, 5,-2]))

























# Cuando lo hagas por tu cuenta, piensa así:

# Empieza en (0,0)
# Define la dirección inicial (arriba)
# Recorre cada número del array:
#  Aplica el movimiento según la dirección
#  Si es negativo, invierte el sentido
#  Actualiza x o y
#  Gira 90° a la izquierda
# Al final, tienes las coordenadas