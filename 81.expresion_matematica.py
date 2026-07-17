#  * Crea una función que reciba una expresión matemática (String)
#  * y compruebe si es correcta. Retornará true o false.
#  * - Para que una expresión matemática sea correcta debe poseer
#  *   un número, una operación y otro número separados por espacios.
#  *   Tantos números y operaciones como queramos.
#  * - Números positivos, negativos, enteros o decimales.
#  * - Operaciones soportadas: + - * / %
#  *
#  * Ejemplos:
#  * "5 + 6 / 7 - 4" -> true
#  * "5 a 6" -> false


#inicio
#obtener operacion
#separarlo por espacio
#para cada elemento de la operacion:
# debe tener un numero
# debe tener una operacion
# si tiene letra o simbolos raros
#  retornar false
#si es true 
# retornar true


def expresion_matematica():
    opes = "5.8 a 6 / 7 - 4"
    spice_list = opes.split()
    # print(spice_list)

    if len(spice_list) % 2 == 0:
        return False
    
    for i, spice in enumerate(spice_list):
        if i % 2 == 0:
            try:
                float(spice)
            except ValueError:
                print(f"no es un numero, ni simbolo: {spice}")
                return False
        else:
            if spice not in "+-*/%":
                return False
        
            
    return True
        


print(expresion_matematica())