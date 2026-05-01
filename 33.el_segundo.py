#  * Dado un listado de números, encuentra el SEGUNDO más grande




#inicio
# ordernar los numeros de mayor a menor
# seleccionar con [] el [1]

def el_segundo():
    lista = [29, 7, 64, 38, 98,89,53, 76, 1,3]
    order = []

    for i in lista:
        pos = 0 
        while pos < len(order) and i < order[pos]:
            pos += 1
        order.insert(pos, i)
    
    seg = order[1]
    return seg

print(el_segundo())



