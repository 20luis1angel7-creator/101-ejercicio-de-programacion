#  * Crea una función que reciba dos parámetros para crear una cuenta atrás.
#  * - El primero, representa el número en el que comienza la cuenta.
#  * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
#  * - Sólo se aceptan números enteros positivos.
#  * - El programa finaliza al llegar a cero.
#  * - Debes imprimir cada número de la cuenta atrás.

#inicio
#obtener los 2 parametros
#

import time

def countdown():
    nums = 5
    speed = 2

    while nums >= 0:
        print(nums)
        time.sleep(speed)
        nums -= 1
    
countdown()