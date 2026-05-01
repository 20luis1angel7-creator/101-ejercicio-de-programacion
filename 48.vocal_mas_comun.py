#  * Crea un función que reciba un texto y retorne la vocal que
#  * más veces se repita.
#  * - Ten cuidado con algunos casos especiales.
#  * - Si no hay vocales podrá devolver vacío.




#inicio
#recibir un texto
#quitar los espacio
#separarlo por letras
#for letra por letra
#si i es una de esta latra
#gruadala en un dicconario con la contidad que hay
#mostrar


def vocal_mas_comun():
    diccionario = {}
    texto = "hola como esta hace tiempo no de se ti"
    texto_separado = list(texto)
    vocal = "aeiou"

    for i in texto_separado:
        if i in vocal:
            if i in diccionario:
                diccionario[i] += 1
            else:
                diccionario[i] = 1
                
    return diccionario
print(vocal_mas_comun())



# def vocal_mas_comun():
#     diccionario = {}
#     texto = "hola como esta hace tiempo no de se ti"
#     texto_separado = list(texto)
#     vocal_a = "a"
#     vocal_e = "e"
#     vocal_i = "i"
#     vocal_o = "o"
#     vocal_u = "u"
#     for i in texto_separado:
#         if i == vocal_a or i == vocal_e or i == vocal_i or i == vocal_o or i == vocal_u:
#             if i in diccionario:
#                 diccionario[i] += 1
#             else:
#                 diccionario[i] = 1
#     return diccionario
# print(vocal_mas_comun())