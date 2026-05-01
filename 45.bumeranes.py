#  * Crea una función que retorne el número total de bumeranes de
#  * un array de números enteros e imprima cada uno de ellos.
#  * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
#  *   seguidos, en el que el primero y el último son iguales, y el segundo
#  *   es diferente. Por ejemplo [2, 1, 2].
#  * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2]
#  *   y [4, 2, 4]).


#inicio
#poner -2 al for
#recorrer el array, lista[j], lista[j + 1], lista[j + 2]
#si lista[j] == lista[j + 2] guardar los valores de los 3
#guardar la cantidad


#optimizado
def boomeran(array):
    boom = []

    for i in range(len(array) - 2):
        a, b, c = array[i], array[i+1], array[i+2]

        if a == c and a != b:
            boom.append((a,b,c))
    
    return boom, len(boom)

print(boomeran([2, 1, 2, 3, 3, 4, 2, 4]))

# def bomeran(array):
    
#     lista = []
#     amount_bomeran = 0

#     for i, _ in enumerate(array[:-2]):

#         if array[i] == array[i+2] and array[i+1] != array[i]:
#             lista.append((array[i],array[i + 1], array[i + 2]))
#             amount_bomeran += 1

#     resul_bomeran = f"cantidad de bomeranes: {amount_bomeran}"
#     return lista, resul_bomeran

# print(bomeran(array = [2, 1, 2, 3, 3, 4, 2, 4]))