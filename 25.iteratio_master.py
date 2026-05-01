#  * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
#  * ¿De cuántas maneras eres capaz de hacerlo?
#  * Crea el código para cada una de ellas.


# def contar1():
#     for i in range(1, 101):
#         print(i)

# contar1()

# def contar2():
#     count =100
#     i=1
#     while i <= count:
#         print(i)
#         i += 1
    
# contar2()

# #recursividad
# def recursividad_conteo(n):
#     print(n)
#     if n == 100:
#         return 100
#     recursividad_conteo(n + 1)
# recursividad_conteo(1)

# #listo
# def con_map():

#     list(map(lambda x: print(x), range(1, 101)))

# con_map()


# def probando(): #listo
#     num = (x + 1 for x in range(0, 100))
#     for n in num:
#         print(n)
# probando()

# def usando_lista():
#     lista = list(range(1, 101))
#     for nu in lista:
#         print(nu)
# usando_lista()

# #listo
# def usando_enumerate():
#     nums = range(1, 101)

#     for i, valor in enumerate(nums, start=1):
        
#         print(i)
# usando_enumerate()



# #listo
# #Generador por comprensión
# def del1_al_100():
#     numero = (x for x in range(1, 101))
#     try:
#         while True:
#             print(next(numero))
#     except StopIteration:
#         pass     #cuando se acaban los numeros, salimos del bucle
    
# del1_al_100()








