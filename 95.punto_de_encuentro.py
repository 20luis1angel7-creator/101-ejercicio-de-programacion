#  * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
#  * en dos dimensiones.
#  * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
#  *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
#  * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
#  * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que
#  *   tardarn en lograrlo.
#  * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.
#  */






# def punto_de_encuentro(x1, vx1, y1, vy1, x2, vx2, y2, vy2):
#     if vx1 == vx2:
#         if x1 != x2:
#             print("no se encuentran")
#             return
        
#     else:
#         t = (x2 - x1) / (vx1 - vx2)

#     pos1 = (x1, y1)
#     vp1 = (vx1, vy1)
#     pos2 =(x2, y2)
#     vp2 = (vx2, vy2)

#     obj1 = x1 + vx1 * t
#     obj2 = x2 + vx2 * t
#     obj3 = y1 + vy1 * t
#     obj4 = y2 + vy2 * t

#     r1 = obj1 == obj2
#     r2 = obj3 == obj4

#     if r1 and r2:
#         print("Se encuentran")
#     else:
#         print("No se encuentran")


# punto_de_encuentro(0, 1, 0, 1, 5, 1, 5, 1)




def punto_de_encuentro(x1, vx1, y1, vy1, x2, vx2, y2, vy2):
    if vx1 != vx2:
        t = (x2 - x1) / (vx1 - vx2)

        if t < 0:
            print("No se encuentran en el futuro")
            return

        y_obj1 = y1 + vy1 * t
        y_obj2 = y2 + vy2 * t

        if abs(y_obj1 - y_obj2) < 1e-9:
            x = x1 + vx1 * t
            print(f"Se encuentran en ({x}, {y_obj1}) después de {t} unidades de tiempo")
        else:
            print("No se encuentran")
    else:
        if x1 != x2:
            print("No se encuentran")
        elif vy1 != vy2:
            t = (y2 - y1) / (vy1 - vy2)

            if t < 0:
                print("No se encuentran en el futuro")
            else:
                y = y1 + vy1 * t
                print(f"Se encuentran en ({x1}, {y}) después de {t} unidades de tiempo")
        elif y1 == y2:
            print("Ya están en el mismo punto y tienen la misma velocidad")
        else:
            print("No se encuentran")

punto_de_encuentro(0, 1, 0, 1, 5, -1, 5, -1)

