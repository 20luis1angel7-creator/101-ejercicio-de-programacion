#  * Crea una función que reciba un número decimal y lo trasforme a Octal
#  * y Hexadecimal.
#  * - No está permitido usar funciones propias del lenguaje de programación que
#  * realicen esas operaciones directamente.



#inicio
#ingresar numero decimal
#obtener el residuo 8 y 16
#un while no sea mayor que numero decimal
# multiplicar (8 o 16) por 1 hasta el 10 
# guargar el ultimo resultado del multi
#obtener el residuo del resultado del while
#se invierte los valores
#hexadecimal se le agregara las letras si es necesario
#mostrar


def decimal_a_octal_hexadecimal():
    decimal = 45

    n = decimal
    octal = ""

    while n > 0:
        residuo = n % 8
        octal = str(residuo) + octal
        n = n // 8
        

    n = decimal 
    hexa = ""
    hexa_map = "0123456789ABCDEF"

    while n > 0:
        residuo = n % 16
        hexa = hexa_map[residuo] + hexa
        n = n // 16

    print(octal)
    print(hexa)

decimal_a_octal_hexadecimal()





# def decimal_a_octal_hexadecimal():
#     decimal = 45
#     residuo_octal = decimal % 8
#     residuo_hexadecimal = decimal % 16

#     r_octal = 0
#     sum_octal = 0
#     r_hexade = 0
#     sum_hexade = 0

#     for i in range(10):
#         r_octal = 8 * i
#         if r_octal < decimal:
#             sum_octal += 1
            
#         r_hexade = 16 * i
#         if r_hexade < decimal:
#             sum_hexade += 1
        
#     residuo_octal2 = sum_octal - 1 % 8
#     residuo_hexadecimal2 = sum_hexade - 1 % 16

#     if residuo_hexadecimal == 10:
#         residuo_hexadecimal = "A"
#     elif residuo_hexadecimal == 11:
#         residuo_hexadecimal = "B"
#     elif residuo_hexadecimal == 12:
#         residuo_hexadecimal = "C"
#     elif residuo_hexadecimal == 13:
#         residuo_hexadecimal = "D"
#     elif residuo_hexadecimal == 14:
#         residuo_hexadecimal = "E"
#     elif residuo_hexadecimal == 15:
#         residuo_hexadecimal = "F"
    
#     print(f"{residuo_hexadecimal2}{residuo_hexadecimal}")
#     print(f"{residuo_octal2}{residuo_octal}")
# decimal_a_octal_hexadecimal()