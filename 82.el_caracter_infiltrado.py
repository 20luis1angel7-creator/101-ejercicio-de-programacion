#  * Crea una función que reciba dos cadenas de texto casi iguales,
#  * a excepción de uno o varios caracteres.
#  * La función debe encontrarlos y retornarlos en formato lista/array.
#  * - Ambas cadenas de texto deben ser iguales en longitud.
#  * - Las cadenas de texto son iguales elemento a elemento.
#  * - No se pueden utilizar operaciones propias del lenguaje
#  *   que lo resuelvan directamente.
#  *
#  * Ejemplos:
#  * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
#  * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]


def caracter_cifrado():
    text1 = "Me llamo.Brais Moure"
    text2 = "Me llamo brais moure"

    list_letter = []

    for i in range(len(text1)):
        if text1[i] != text2[i]:
            list_letter.append(text2[i])
    
    print(list_letter)
caracter_cifrado()