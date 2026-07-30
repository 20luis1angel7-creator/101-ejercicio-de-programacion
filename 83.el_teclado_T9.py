#  * Los primeros dispositivos móviles tenían un teclado llamado T9
#  * con el que se podía escribir texto utilizando únicamente su
#  * teclado numérico (del 0 al 9).
#  *
#  * Crea una función que transforme las pulsaciones del T9 a su
#  * representación con letras.
#  * - Debes buscar cuál era su correspondencia original
#  * - Cada bloque de pulsaciones va separado por un guión.
#  * - Si un bloque tiene más de un número, debe ser siempre el mismo.
#  * - Ejemplo:
#  *     Entrada: 6-666-88-777-33-3-33-888
#  *     Salida: M


#inicio
#obtener la entrada
#separarlo por los guiones
#obtener los valores que tiene los numero
#recorrer numero separado por el guion
# si es 1 o otro numero
#  mensaje de error
# obtener la cantidad de numero para tener la letra
# guardar esa letra
#mostrar

def teclado_T9():
    Entrada = "6-666-88-777-33-3-33-888"

    sepa = Entrada.split("-")
    print(sepa)
    n = []

    letras = {
        "2": ("A", "B", "C"),
        "3": ("D", "E", "F"),
        "4": ("G", "H", "I"),
        "5": ("J", "K", "L"),
        "6": ("M", "N", "O"),
        "7": ("P", "Q", "R", "S"),
        "8": ("T", "U", "V"),
        "9": ("W", "X", "Y", "Z")
    }

    for sep in sepa:
        if sep <= 1 or sep >= 10:
            print("error debe de ser un numero de 2 al 9")
            
        valor = sep[0]
        cant = len(sep)

        n += letras[valor][cant - 1]

    print(n)
teclado_T9()