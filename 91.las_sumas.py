# /*
#  * Crea una función que encuentre todas las combinaciones de los números
#  * de una lista que suman el valor objetivo.
#  * - La función recibirá una lista de números enteros positivos
#  *   y un valor objetivo.
#  * - Para obtener las combinaciones sólo se puede usar
#  *   una vez cada elemento de la lista (pero pueden existir
#  *   elementos repetidos en ella).
#  * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
#  *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
#  *   (Si no existen combinaciones, retornar una lista vacía)
#  */

#1. Recursividad 
#2. Backtracking 
#3. Arrays/listas y recorrido por índices 
#4. Combinaciones vs. permutaciones
#5. Complejidad temporal 
#6. Manejo de elementos repetidos

def sumas(lista, objetivo, indice, sumaActual, combinacion):
    if (sumaActual == objetivo):
        return combinacion
    if (sumaActual < objetivo):
        sumaActual += lista[indice]
        combinacion.append(lista[indice])
        print("suma:", sumaActual)
        print(combinacion)

        print(indice)
        print(lista[indice])

        

        result = sumas(lista, objetivo, indice + 1, sumaActual, combinacion)

    if (indice == len(lista)):
        return sumaActual
    
sumas([1, 5, 3, 2], 6, 0, 0, [])