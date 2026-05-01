#  * Crea una función que transforme grados Celsius en Fahrenheit
#  * y viceversa.
#  *
#  * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
#  *   y su unidad ("C" o "F").
#  * - En caso contrario retornará un error.



def conversor(dato):

    if dato[-2] != "°":
        return "Error no tiene °"

    if dato[-1] == "C":
        divi = 9 / 5
        F = (float(dato[:-2]) * divi) + 32
        return F
    elif dato[-1] == "F":
        divi = 5 / 9
        C = (float(dato[:-2]) - 32) * divi
        return C
    else:
        return "Error"

print(conversor("77 °F"))




