#  * Crea un programa que determine si dos vectores son ortogonales.
#  * - Los dos array deben tener la misma longitud.
#  * - Cada vector se podría representar como un array. Ejemplo: [1, -2]


#inicio
#obtenemos a y b
#cojemos la primera de la a y b
#cogemos la segunda de la a y b
#luego lo multiplicamos
#si un numero es negativo se resta
#sino se suma
#si = 0 es ortogonales
#sino no lo son


def vectores_ortogonales(a, b):
    
    result_a = a[0] * b[0]
    result_b = a[1] * b[1]

    resultado = result_a + result_b

    if(resultado == 0):
        print(resultado, "es ortogonal")
    else:
        print(resultado, "no es ortogonal")



vectores_ortogonales([1, -2],[2, 1])


