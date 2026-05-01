#  * Crea un programa se encargue de transformar un número binario
#  * a decimal sin utilizar funciones propias del lenguaje que
#  * lo hagan directamente.









# binario a decimal
def sumar(container):
    suma = 0
    for c in container:
        suma += c
    return suma

def binario_a_decimal():
    binario = "1011"
    len_binario = len(binario) - 1
    container = []

    for b in binario:
        multi = int(b) * 2 ** len_binario
        container.append(multi)
        len_binario -= 1

    result = sumar(container)

    print(result)

binario_a_decimal()






#decimal a binaio

# def decimal_a_binario():
#     num = 10
#     almacen=[]

#     while num > 0:
#         resultado = num % 2
#         almacen.append(resultado)
#         act = num // 2
#         num = act
#     orden = almacen[::-1]
#     print(orden)

# decimal_a_binario()
