#  * Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
#  * indicándole únicamente el tamaño del lado.
#  *
#  * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
#  *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif


# inicio
# tenemos un [1]
#repetir varias veces
# agregamos al inicio [1] 
# for que recorra el array ej:lista[i] + lista[i + 1]
#agregar resultado
# al terminar [1]
# guardar lista







def pascal():
    n = 5
    num = 1
    lista = [1,1]
    list_vacia = []
    print([1])
    print(lista)

    #for _ in range(n):     el for y while aqui hacer lo mismo
    while n > 0:
        list_vacia.append(num)

        for i in range(len(lista) - 1):
            suma = lista[i] + lista[i + 1]
            list_vacia.append(suma)
        
        list_vacia.append(num)

        print(list_vacia)

        lista = list_vacia
        list_vacia = []

        n -= 1
pascal()

































# def pascal():
#     num = 5
#     inicio = 1
#     lista =[1, 1]
#     list_vacia =[]
#     print(inicio)
#     print(lista)

#     while num > 0:
#         list_vacia.append(inicio)

#         for i in range(len(lista) - 1):  
#             suma = lista[i] + lista[i + 1]
#             list_vacia.append(suma)
        
#         list_vacia.append(inicio)    
            
#         print(list_vacia)
#         lista = list_vacia
#         list_vacia = []
#         num -= 1

# pascal()