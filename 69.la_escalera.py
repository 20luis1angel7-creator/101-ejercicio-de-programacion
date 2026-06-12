#  * Crea una función que dibuje una escalera según su número de escalones.
#  * - Si el número es positivo, será ascendente de izquiera a derecha.
#  * - Si el número es negativo, será descendente de izquiera a derecha.
#  * - Si el número es cero, se dibujarán dos guiones bajos (__).
#  *
#  * Ejemplo: 4
#  *         _
#  *       _|
#  *     _|
#  *   _|
#  * _|
#  *


#inicio
#obtener n escalon
#si es positivo
# n * 2 y ahi se pondra _
# se restara 2 y pondra _|
#si es negativo 
# comienza desde el inicio con _
# si es 0 sumara 1 y pondra |_
# sino sumara 2 y pondra |_
#si n es 0 mostrar __



def la_escalera():
    n = -6

    if n > 0:
        sum_for_two = n * 2

        print(" " * sum_for_two + "_")
        sum_for_two -= 2

        while sum_for_two >= 0:
            print(" " * sum_for_two + "_|")
            sum_for_two -= 2

    if n < 0:
        sum_for_two = n * 2
        sum_positive = abs(sum_for_two)
        print(sum_positive)
        m = 0

        print("_")
        m += 1

        while m <= sum_positive:
            print(" " * m + "|_")
            m += 2

    if n == 0:
        print("__")
la_escalera()
