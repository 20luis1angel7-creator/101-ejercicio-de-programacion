#  * Crea una función que dibuje una espiral como la del ejemplo.
#  * - Únicamente se indica de forma dinámica el tamaño del lado.
#  * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
#  *
#  * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
#  * ════╗
#  * ╔══╗║
#  * ║╔╗║║
#  * ║╚═╝║
#  * ╚═══╝


def espiral(n):
    matriz = [[" " for _ in range(n)] for _ in range(n)]

    capa = 0

    while capa < (n + 1) // 2:
        ini = capa
        fin = n - capa - 1

        for j in range(ini, fin):
            matriz[ini][j] = "═"
        matriz[ini][fin] = "╗"

        for i in range(ini + 1, fin + 1):
            matriz[i][fin] = "║"

        if fin > ini:
            matriz[fin][fin] = "╝"
            for j in range(fin - 1, ini - 1, - 1):
                matriz[fin][j] = "═"
            
        if fin - ini > 1:
            matriz[fin][ini] = "╚"
            for i in range(fin - 1, ini + 1, - 1):
                matriz[i][ini] = "║"

        if capa + 1 < (n + 1) // 2:
            matriz[ini + 1][ini] = "╔"

        capa += 1

    if n % 2 == 1:
        c = n // 2
        matriz[c][c] = "╗"
        matriz[c][c-1] = "╔"

    for fila in matriz:
        print("".join(fila))

espiral(5)


























# def espiral(n):
#     matriz = [[" " for _ in range(n)] for _ in range(n)]

#     # Dibujamos la espiral por capas
#     capa = 0

#     while capa < (n + 1) // 2:
#         ini = capa
#         fin = n - capa - 1

#         # Horizontal superior
#         for j in range(ini, fin):
#             matriz[ini][j] = "═"
#         matriz[ini][fin] = "╗"

#         # Vertical derecha
#         for i in range(ini + 1, fin + 1):
#             matriz[i][fin] = "║"

#         # Horizontal inferior
#         if fin > ini:
#             matriz[fin][fin] = "╝"
#             for j in range(fin - 1, ini - 1, -1):
#                 matriz[fin][j] = "═"

#         # Vertical izquierda dejando la entrada
#         if fin - ini > 1:
#             matriz[fin][ini] = "╚"
#             for i in range(fin - 1, ini + 1, -1):
#                 matriz[i][ini] = "║"

#         # Entrada de la siguiente vuelta
#         if capa + 1 < (n + 1) // 2:
#             matriz[ini + 1][ini] = "╔"

#         capa += 1

#     # Corregir el centro
#     if n % 2 == 1:
#         c = n // 2
#         matriz[c][c] = "╝"
#         matriz[c][c-1] = "╚"

#     for fila in matriz:
#         print("".join(fila))


# espiral(5)