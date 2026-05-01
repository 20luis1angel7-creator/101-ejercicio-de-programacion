#  * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
#  * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
#  * - EXTRA: ¿Eres capaz de dibujar más figuras?
 
# n=5
# for i in range(n):
#     if i == 0 or i == n -1:
#         print("*" *n)
#     else:
#         print("*" + " " * (n - 2) + "*")


# n = 5
# for i in range(1, n + 1):
#     print("*" * i)
# *
# **
# ***
# ****
# *****

# n = 5 
# for i in range(1, n + 1):
#     print(" "* (n - i) + "*" * (2* i -1))
#     *
#    ***
#   *****
#  *******
# *********

# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2*i-1))
# for j in range(n - 1, 0, -1):
#     print(" " * (n - j) + "*" * (2*j-1))
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


# n = 5
# for j in range(1, n + 1): 
#     print(" " * (n - j) + "*" * (2*j-1))
# for i in range(1, n + 1):
#     print(" " * (n-1) + "*")
#     *
#    ***
#   *****
#  *******
# *********
#     *
#     *
#     *
#     *
#     *



# n = 5
# for j in range(n - 1, 0, -1):
#     print(" "* (n - j) + "*" * (2*j-1))
# for i in range(2, n + 1):
#     print(" " * (n - i)+ "*" * (2 * i - 1))
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********



































