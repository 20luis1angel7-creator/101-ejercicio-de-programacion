#  * Crea una función que reciba dos array, un booleano y retorne un array.
#  * - Si el booleano es verdadero buscará y retornará los elementos comunes
#  *   de los dos array.
#  * - Si el booleano es falso buscará y retornará los elementos no comunes
#  *   de los dos array.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.

#inicio
#crear las lista
#ingresar 2 array y un booleano
#leer los dos array
#si es true
#buscar los elementos comunes entre ellos
#si es false
#buscar los elementos no comunes entre ellos
#retornar el resultado



def readlisttwoarrays(arrayone, arraytwo, esta):
    resultado = []

    for array1 in arrayone:
        encontrado = False

        for array2 in arraytwo:
            if array1 == array2:
                encontrado = True
                break
        
        if esta == True:
            if encontrado:
                resultado.append(array1)
        else:
            if not encontrado:
                resultado.append(array1)
        
    if esta == False:
        for array2 in arraytwo:
            encontrado = False

            for array1 in arrayone:
                if array2 == array1:
                    encontrado = True
                    break
            
            if not encontrado:
                resultado.append(array2)
    return resultado

listone = [1,2,3,4,5,6,7,8]
listtwo =[2,4,6,8]
print(readlisttwoarrays(listone, listtwo, True))
print(readlisttwoarrays(listone, listtwo, False))

























# listone = [1,2,3,4,5,6,7,8]
# listtwo = [2,4,6,8]

# estado = False


# def readlisttwoarrays(arrayone, arraytwo, esta):
#     resultado =[]

#     for array1 in arrayone:
#         encontrado = False

#         for array2 in arraytwo:
#             if array1 == array2:
#                 encontrado = True
#                 break
                
            

#     if esta == True:    
#         if encontrado == True:
#             resultado.append(array1)
#             print(resultado)
        
#     if esta == False:
#             if encontrado == False:
#                 resultado.append(array2)
#                 print(resultado)

        
                
















    # if esta == True:
    #     repetidos = list(set(arrayone) and list(set(arraytwo)))
    #     return repetidos
        
    # if esta == False:
    #     no_repetidos = list(set(arrayone) ^ set(arraytwo))
    #     return no_repetidos




            
                



        # if arraytrue != array1:
        #     arrayfalse1.append(array1)
        #     print(arrayfalse1, "fa")
        # if arraytrue != array2:
        #     arrayfalse2.append(array2)
    # if arrayone != arraytwo:
    #     arrayfalse1.append(arrayone)
    #     arrayfalse2.append(arraytwo)
    #     print(arrayfalse1)
    #     print(arrayfalse2)
    # arrayfalse1 ==

# r = readlisttwoarrays(listone, listtwo, estado)
# print(r)








