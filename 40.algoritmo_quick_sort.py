#  * Implementa uno de los algoritmos de ordenación más famosos:
#  * el "Quick Sort", creado por C.A.R. Hoare.
#  * - Entender el funcionamiento de los algoritmos más utilizados de la historia
#  *   Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
#  *   Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
#  * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
#  *   donde trabajaremos y entenderemos los más famosos de la historia.
 






def quick_sort(lista):
    # if len(lista) <= lista[1]:
    #     return ord
    if len(lista) <= 1:
        return lista
    
    alm_mayor = []
    alm_menor = []
    ord=[]

    pivote = lista[0]

    for i in lista[1:]:
        if i > pivote:
            alm_mayor.append(i)
            
            print(alm_mayor)
        elif i < pivote:
            alm_menor.append(i)
            print(alm_menor)

    mayores_ordenadas = quick_sort(alm_mayor)
    menores_ordenadas = quick_sort(alm_menor)

    piv = []
    piv.append(pivote)
    ord = menores_ordenadas + piv + mayores_ordenadas
    return ord
        
print(quick_sort(lista = [11,4,9,20,2,10,30,5,3,24]))


















# def insertion_sort():
#     lista = [9,8,7,6,5,4,3,40,50,0,1,2,10]
#     for i in range(1, len(lista)):
#         clave = lista[i]
#         j = i - 1
#         while j >= 0 and lista[j] > clave:
#             lista[j + 1] = lista[j]
#             j-= 1
#         lista[j + 1] = clave
#     return lista
# print(insertion_sort()) 

# def selection_sort():
#     lista = [9,8,7,6,5,4,3,40,50,0,1,2,10]
#     n = len(lista)
#     for i in range(n):
#         min_ele = i
#         for j in range(i + 1, n):
#             if lista[j] < lista[min_ele]:
#                 lista[min_ele], lista[j] = lista[j], lista[min_ele]
#     return lista
# print(selection_sort())

# def bubble_sort():
#     lista = [9,8,7,6,5,4,3,40,50,0,1,2,10]
#     n = len(lista)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#                 print(lista)
#     return lista
# print(bubble_sort())