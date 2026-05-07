#  * Crea tu propio enunciado para que forme parte de los retos de 2023.
#  * - Ten en cuenta que su dificultad debe ser asumible por la comunidad y seguir
#  * un estilosemejante a los que hemos realizado durante el año.
#  * - Si quieres también puedes proponer tu propia solución al reto
#  *   (en el lenguaje que quieras).

# el promedio de un grupo de numero (como loteria)

#inicio
#grupo de numero 3 en 3 (dict o list)
#for de todo ese grupo
# se coge el primer indice
# se cuenta la cantidad de numero
# se suma todos los numeros de ese indice
# se divide


def promedio_numeros():
    numeros = [
        [12, 34, 45],
        [5, 22, 39],
        [18, 27, 41],
        [9, 16, 33],
        [7, 25, 48],
        [3, 19, 44],
        [11, 28, 36],
        [2, 14, 40],
        [6, 21, 47],
        [10, 30, 42],
        [8, 17, 35],
        [4, 23, 46],
        [13, 26, 38],
        [15, 24, 43],
        [1, 29, 37]
    ]
    
    index_0 = 0
    index_1 = 0
    index_2 = 0

    for i in numeros:
        index_0 += i[0] / 3 
        index_1 += i[1] / 3
        index_2 += i[2] / 3
        
    print(index_0, index_1, index_2)
    
        
promedio_numeros()