#  * Crea una función que calcule el número de la columna de una hoja de Excel
#  * teniendo en cuenta su nombre.
#  * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
#  * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.

#creado por mi

#inicio
#obtener el abecedario
#recorrer el abecedario
# recorrer cada elemento del abecedario
#  sumar 1 en cada elemento
#  si es igual o mayor al elemento 
#   parar de recorrer
#mostrar la suma y el elemento

#correccion
# Inicio
# Recibir el nombre de la columna.
# Inicializar una variable resultado en 0.
# Recorrer cada letra del nombre de la columna.
# Obtener el valor de la letra (A = 1, B = 2, ..., Z = 26).
# Multiplicar el resultado actual por 26.
# Sumar el valor de la letra al resultado.
# Repetir el proceso hasta recorrer todas las letras.
# Mostrar el resultado.
# Fin

def la_columna_de_excel():
    nombre_columna = "AA"
    sumar = 0

    valores = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26
    }
    for i in nombre_columna:
        print(i, valores[i])
        sumar = sumar * 26 + valores[i]
        print(sumar)

la_columna_de_excel()