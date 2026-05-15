#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)


#inicio
#longitud?
#letras mayuscula?
#numeros?
#simbolos?
#for de 8 o 16:
# si letras mayuscuta es true
#  listas de letras mayuscula
#  random 
# si numero es true 
#  lista de numeros
#  random
# si simbolo es true
#  lista de simbolos
#  random
# si letras es true
#  listas de letras
#  random 
#mostrar contrasena

import random

def generated_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = []

    password += "".join(random.choices(letters, k=16))
    print("".join(password))
generated_password()


# def generated_password():
#     length = 16
#     capital_letter = True
#     numbers = True
#     symbols = True

#     amount_numbers = 1
#     amount_capital = 1
#     amount_symbols = 1

#     password = []
#     for i in range(1, length + 1):
#         if capital_letter is True and (length == 8 and amount_capital <= 2 or length == 16 and amount_capital <= 4):
#             list_capital_letter = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
#             password += random.choices(list_capital_letter)
#             amount_capital += 1
#         if numbers is True and (length == 8 and amount_numbers <= 2 or length == 16 and amount_numbers <= 4):
#             lists_numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
#             password += random.choices(lists_numbers)
#             amount_numbers += 1
#         if symbols is True and (length == 8 and amount_symbols <= 2 or length == 16 and amount_symbols <= 4):
#             lists_symbols = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", ",", ".", "/", "?", "\\", "|", "<", ">")
#             password += random.choices(lists_symbols)
#             amount_symbols += 1
#         lists_letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
#         password += random.choices(lists_letters)
#     pass_join = "".join(password)
#     print(pass_join)
# generated_password()