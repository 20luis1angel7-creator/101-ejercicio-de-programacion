# /*
#  * Crea un programa que sea capaz de generar e imprimir todas las
#  * permutaciones disponibles formadas por las letras de una palabra.
#  * - Las palabras generadas no tienen por qué existir.
#  * - Deben usarse todas las letras en cada permutación.
#  * - Ejemplo: sol, slo, ols, osl, los, lso
#  */

#a estudiar
# Listas
# Strings
# for
# Funciones
# Recursividad
# Backtracking
# Permutaciones/factorial


#inicio
#ingresar palabras
#separarlo en letras
#elegir una letra
#agregar esa letra a una nueva combinacion
#elegir otra letra que todavia no hayas utilizado
#repetir hasta utilizar todas las letras
#cuando hayas utilizado todas, mostrar la combinacion
#volver atra y probar otra combinacion
#cuando ya no queden combinaciones, terminar



def combinaciones(word, combinar, utilizadas):
    
    letters = list(word)
    # print(letters)
    for i in word:
        if i in utilizadas:
            print("kkkk")
            continue
        print(i)
        utilizadas.append(i)
        combinar.append(i)
        print(combinar)
        combinaciones(word, combinar, utilizadas)
        combinar.pop()
        print(utilizadas)
        if len(combinar) == len(letters):
            return print("".join(combinar))
        
        
        

combinaciones("sol", [], [])