#  * Dado un array de enteros ordenado y sin repetidos,
#  * crea una función que calcule y retorne todos los que faltan entre
#  * el mayor y el menor.
#  * - Lanza un error si el array de entrada no es correcto.


#inicio
#obtener el array
# si el array no esta ordenado => error
#for que coja el numero mas bajo y alto
#para cada numero de este array
# si este numero existe continuar
# sino agregarlo



def array_enteros(lista):
    numero = 0
    #comprovar si estan en orden
    for o in lista:
        if o > numero:
            numero = o
        else:
            return "array is not order"
        
    #generar todos los numeros
    guardar = []
    for i in range(lista[0], lista[-1] + 1):
        guardar.append(i)

    #eliminar duplicado
    result = list(set(guardar) - set(lista))
    return result
    
print(array_enteros([1,5,12, 15,18]))





















