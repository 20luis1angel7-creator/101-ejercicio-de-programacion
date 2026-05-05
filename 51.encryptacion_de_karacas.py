#  * Crea una función que sea capaz de encriptar y desencriptar texto
#  * utilizando el algoritmo de encriptación de Karaca
#  * (debes buscar información sobre él).

#inicio
#obtener texto
#invertirlo
#cambiar vocales por numeros
#poner aca al final
#quitar aca
#cambiar numeros por vocales
#invertirlo


# def encryption():
#     word = "encriptacion"

#     invest = word[::-1]

#     replacement = {
#         "a": "0",
#         "e": "1",
#         "i": "2",
#         "o": "2",
#         "u": "3",
#     }

#     result = ""

#     for letter in invest:
#         if letter in replacement:
#             result += replacement[letter]
#         else:
#             result += letter
        
#     result += "aca"

#     print(result)
    
# encryption()

def encryption(word):
    replacement = str.maketrans("aeiou", "01223")
    return word[::-1].translate(replacement) + "aca"

print(encryption("luis"))