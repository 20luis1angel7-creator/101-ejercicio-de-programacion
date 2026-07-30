#  * Crea una función que sea capaz de leer el número representado por el ábaco.
#  * - El ábaco se representa por un array con 7 elementos.
#  * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
#  *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
#  * - El primer elemento del array representa los millones, y el último las unidades.
#  * - El número en cada elemento se representa por las cuentas que están a
#  *   la izquierda del alambre.
#  *
#  * Ejemplo de array y resultado:
#  * ["O---OOOOOOOO",
#  *  "OOO---OOOOOO",
#  *  "---OOOOOOOOO",
#  *  "OO---OOOOOOO",
#  *  "OOOOOOO---OO",
#  *  "OOOOOOOOO---",
#  *  "---OOOOOOOOO"]
#  *
#  *  Resultado: 1.302.790


#inicio
#obtener array
#recorrer el array
# contar la posicion antes del ---
# mostrar 


def el_abaco():
    lis = []
    array = [
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO"
        ]

    for i in array:
        lis.append(i.find("---"))

    r = int("".join(map(str, lis)))
    print(f"{r:,}")

















    
    # for i in array:
    #     lis.append(i.find("---"))

    # print(lis)
    # juntos = int(''.join(map(str, lis)))
    # result = f"{juntos:,}"
    # print(result)
el_abaco()