#  * ¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
#  *
#  * Crea un programa que dibuje una Trifuerza de "Zelda"
#  * formada por asteriscos.
#  * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
#  * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#  *
#  * Ejemplo: Trifuerza 2
#  *
#  *    *
#  *   ***
#  *  *   *
#  * *** ***

def trifuerza():
    n = 2

    # Triángulo superior
    for i in range(n):
        print(" " * (2 * n - i - 1) + "*" * (2 * i + 1))

    # Triángulos inferiores
    for i in range(n):
        espacios_centro = 2 * (n - i) - 1
        print(" " * (n - i - 1) +
              "*" * (2 * i + 1) +
              " " * espacios_centro +
              "*" * (2 * i + 1))

trifuerza()