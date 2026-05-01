#  * Crea una función que ordene y retorne una matriz de números.
#  * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
#  *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#  *   o de mayor a menor.
#  * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
#  *   automáticamente.


def ordenar_lista(lista, ordenamiento):
    
    

    order = []
    for i in lista:
        pos = 0
        if ordenamiento == "Asc":
            while pos < len(order) and i > order[pos]:
                pos +=1
            order.insert(pos, i)
        elif ordenamiento == "Desc":
            while pos < len(order) and i < order[pos]:
                pos += 1
            order.insert(pos, i)
        else:
            print("error")
    print(order)
    return order
























    
    # orden = []
    # for l in lista:
    #     arr = 0
    #     if ordenamiento == "Asc":
    #         while arr < len(orden) and l > orden[arr]:
    #             arr += 1
    #         orden.insert(arr, l)
    #     elif ordenamiento == "Desc":
    #         while arr < len(orden) and l < orden[arr]:
    #             arr += 1
    #         orden.insert(arr, l)    
    #     else:
    #         print("el ordenamiento es incorrecto debe ser Asc o Desc")
    #     print(orden)
    # return orden

    # for i in range(len(lista)):
    #     for j in range(i + 1, len(lista)):
    #         if ordenamiento == "Asc":
    #             if lista[i] > lista[j]:
    #                 lista[i], lista[j] = lista[j], lista[i]
    #         elif ordenamiento == "Desc":
    #             if lista[i] < lista[j]:
    #                 lista[i], lista[j] = lista[j], lista[i]
    # print(lista)
    # return lista





print(ordenar_lista(lista = [73, 12, 98, 45, 6, 31, 84, 27, 59, 14], ordenamiento="Asc"))





