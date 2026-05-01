#  * Simula el funcionamiento de una máquina expendedora creando una operación
#  * que reciba dinero (array de monedas) y un número que indique la selección
#  * del producto.
#  * - El programa retornará el nombre del producto y un array con el dinero
#  *   de vuelta (con el menor número de monedas).
#  * - Si el dinero es insuficiente o el número de producto no existe,
#  *   deberá indicarse con un mensaje y retornar todas las monedas.
#  * - Si no hay dinero de vuelta, el array se retornará vacío.
#  * - Para que resulte más simple, trabajaremos en céntimos con monedas
#  *   de 5, 10, 50, 100 y 200.
#  * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
 
#inicio
#obtenenmos el array y el numero
#creamos una lista de numero(productos)
#sumamos el array
#si el numero = numero(productos) y el array > numero(producto)
# array - numero(p) = result
#n = 200
#while n = 0
# si result < n
# se agrega
# continue


#mostrar nombre del producto y arrar


def maquin_expendedora(product, array):
    
    lista_productos = ("apple", "banana", "watermalon", "orange", "grape")
    precio_producto = (50, 115, 150, 100, 50)
    product1 = product - 1 
    precio1 = product - 1
    if product < 0 or product > len(lista_productos):
        raise ValueError("no hay ese producto")
    else:
        print(lista_productos[product1], precio_producto[precio1])
    

    suma = 0
    for s in array:
        suma += s
    # print(suma)
        
    resta = suma - precio_producto[product1]

    devuelta = 0
    suma_devuelta = []
    array = array[::-1]

    for i in array:
        if  i <= resta:

            resta -= i 
            
            devuelta += i
            suma_devuelta.append(i)
    
    
    if resta != 0:
        raise ValueError("error, esa cantidad de moneda no hay, vuelva mas tarde")
    
    return devuelta, suma_devuelta



print(maquin_expendedora(product = 1, array = (5,10,50,100,200)))





# def maquin_expendedora(product, array):
#     lista_productos = ("apple", "banana")
#     precio_producto = (50, 125)

#     product1 = product - 1

#     if product1 < 0 or product1 >= len(lista_productos):
#         raise ValueError("No existe ese producto")

#     print(lista_productos[product1], precio_producto[product1])

#     # Sumar dinero ingresado
#     suma = sum(array)

#     # Verificar dinero suficiente
#     if suma < precio_producto[product1]:
#         raise ValueError("Dinero insuficiente")

#     resta = suma - precio_producto[product1]

#     # Devolución con menor número de monedas
#     monedas = [200, 100, 50, 10, 5]
#     devuelta = []

#     for m in monedas:
#         while resta >= m:
#             resta -= m
#             devuelta.append(m)

#     # Si resta no llegó a 0, significa que no se pudo devolver exactamente
#     if resta != 0:
#         raise ValueError("No se puede devolver cambio exacto")

#     return lista_productos[product1], devuelta