# /*
#  * Crea una función que encuentre todos los triples pitagóricos
#  * (ternas) menores o iguales a un número dado.
#  * - Debes buscar información sobre qué es un triple pitagórico.
#  * - La función únicamente recibe el número máximo que puede
#  *   aparecer en el triple.
#  * - Ejemplo: Los triples menores o iguales a 10 están
#  *   formados por (3, 4, 5) y (6, 8, 10).
#  */

import math

def triple_pitagorico(n):
    lista_sum_number = []
    result = []
    for i in range(1, n + 1):
        multi = i * i
        lista_sum_number.append(multi)

    for l in lista_sum_number:
        for s in lista_sum_number:
            suma = s + l
            if suma == lista_sum_number[-1]:
                print(
                    int(math.sqrt(s)),
                    int(math.sqrt(l)),
                    int(math.sqrt(suma))
                )
                

    print(lista_sum_number)
triple_pitagorico(5)
