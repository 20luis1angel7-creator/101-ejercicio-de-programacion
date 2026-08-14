#  * Crea un programa capaz de gestionar una pieza de Tetris.
#  * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
#  * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
#  *   🔳
#  *   🔳🔳🔳
#  * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
#  *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
#  *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en
#  *   la pantalla de juego.
#  * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
#  * - Debes tener en cuenta los límites de la pantalla de juego.
#  */



#a estudiar antes de empezar

#  Matrices (listas de listas)
# Cómo representar un tablero de 10x10.
# Acceder y modificar una celda usando índices (tablero[fila][columna]).
#  Coordenadas (fila y columna)
# Cómo representar una posición mediante (fila, columna).
# Cómo mover una posición sumando o restando valores.
#  Representación de figuras
# Cómo guardar una pieza como un conjunto de coordenadas relativas.
# Diferencia entre la posición de la pieza y su forma.
#  Funciones
# Crear funciones con una única responsabilidad.
# Por ejemplo, una función que dibuje el tablero, otra que mueva la pieza, etc.
#  Condicionales
# Verificar si un movimiento es válido.
# Comprobar que no se salga de los límites del tablero.
#  Bucles
# Recorrer todas las celdas del tablero.
# Recorrer todos los bloques que forman la pieza.
#  Transformaciones geométricas básicas
# Entender qué significa rotar una figura 90°.
# Cómo cambian las coordenadas de una pieza al rotarla.
#  Validación de movimientos
# Comprobar si una acción puede realizarse antes de aplicarla.
# Detectar cuándo una pieza chocaría con un borde.
#  Estado del programa
# Comprender qué información debe mantenerse entre llamadas:
# posición actual,
# orientación actual,
# tablero actual.
# Abstracción y diseño
# Pensar el problema dividiéndolo en pequeñas tareas en lugar de intentar resolverlo todo de una vez.

FILAS = 10
COLUMNAS = 10

# Pieza inicial:
# 🔳
# 🔳🔳🔳
PIEZA = [
    [1, 0, 0],
    [1, 1, 1]
]

# Posición inicial: esquina superior izquierda
pieza_fila = 0
pieza_columna = 0


def rotar_pieza(pieza):
    """Rota la pieza 90 grados en sentido horario."""
    filas = len(pieza)
    columnas = len(pieza[0])

    return [
        [pieza[filas - 1 - f][c] for f in range(filas)]
        for c in range(columnas)
    ]


def puede_colocar(pieza, fila, columna):
    """Comprueba que la pieza cabe dentro del tablero."""
    for f in range(len(pieza)):
        for c in range(len(pieza[0])):
            if pieza[f][c] == 1:
                nueva_fila = fila + f
                nueva_columna = columna + c

                if nueva_fila < 0 or nueva_fila >= FILAS:
                    return False

                if nueva_columna < 0 or nueva_columna >= COLUMNAS:
                    return False

    return True


def mostrar_tablero():
    """Muestra el tablero de 10x10 con la pieza."""
    tablero = [
        ["🔲" for _ in range(COLUMNAS)]
        for _ in range(FILAS)
    ]

    for f in range(len(PIEZA)):
        for c in range(len(PIEZA[0])):
            if PIEZA[f][c] == 1:
                tablero[pieza_fila + f][pieza_columna + c] = "🔳"

    for fila in tablero:
        print("".join(fila))

    print()


def ejecutar_accion(accion):
    """Ejecuta una acción sobre la pieza."""

    global PIEZA
    global pieza_fila
    global pieza_columna

    nueva_fila = pieza_fila
    nueva_columna = pieza_columna
    nueva_pieza = PIEZA

    if accion == "derecha":
        nueva_columna += 1

    elif accion == "izquierda":
        nueva_columna -= 1

    elif accion == "abajo":
        nueva_fila += 1

    elif accion == "rotar":
        nueva_pieza = rotar_pieza(PIEZA)

    else:
        print("Acción no válida.")
        return

    # Solo aplicamos el movimiento/rotación si es válido
    if puede_colocar(nueva_pieza, nueva_fila, nueva_columna):
        PIEZA = nueva_pieza
        pieza_fila = nueva_fila
        pieza_columna = nueva_columna

    mostrar_tablero()


# Mostrar la posición inicial
mostrar_tablero()

# Ejemplos de acciones
ejecutar_accion("derecha")
ejecutar_accion("derecha")
ejecutar_accion("abajo")
ejecutar_accion("rotar")
ejecutar_accion("abajo")
ejecutar_accion("abajo")
ejecutar_accion("abajo")
ejecutar_accion("abajo")
ejecutar_accion("abajo")
ejecutar_accion("rotar")
ejecutar_accion("rotar")
ejecutar_accion("rotar")
ejecutar_accion("abajo")
ejecutar_accion("abajo")