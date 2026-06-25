#  * Crea un programa que encuentre y muestre todos los pares de números primos
#  * gemelos en un rango concreto.
#  * El programa recibirá el rango máximo como número entero positivo.
#  *
#  * - Un par de números primos se considera gemelo si la diferencia entre
#  *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#  *
#  * - Ejemplo: Rango 14
#  *   (3, 5), (5, 7), (11, 13)


#inicio
#n es el rango
#para cada rango de n
# sacar los numeros primos
# guardarlo
# si comparamos el ultimo con el de ahora y si se lleva 2 de diferencia 
#  lo guardamos en un lista
#lo mostramos


def primos():
    n = 100
    is_primo = []

    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            is_primo.append(i)
    
    gemelos = []

    for i in range(len(is_primo) - 1):
        if is_primo[i + 1] - is_primo[i] == 2:
            gemelos.append((is_primo[i], is_primo[i + 1]))
    print(gemelos)

primos()

# def num_primos_gemelos():
#     num = 10
#     print(primos(num))

#     print()

# num_primos_gemelos()