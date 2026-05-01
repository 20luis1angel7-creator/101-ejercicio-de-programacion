 # Escribe un programa que se encargue de comprobar si un número es o no primo.
 # Hecho esto, imprime los números primos entre 1 y 100.



#ingresar el numero
#hacer un for para recorrer cada numero
#si es par no es primo
#se divide por 1 o por el mismo (es primo) (ej: 2/1=2, 7/1=7)
#si se divide por mas ya no es primo (ej: 8/4=2, 10/5=2)
#(cuando esta divide un numero, el resultado no puede ser un numero entero)


import math

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0: #los pares false
        return False
    
    #saca la raiz
    limite = int(math.sqrt(n))

    #probar solo divisores impares (empieza con 3, limite + 1: llega hasta la raiz cuadrada)
    for divisor in range(3, limite + 1, 2):  #avanza de 2 en 2: 3,5,7,9,11...
        #revisa si hay divisor ecxacto
        if n % divisor == 0:
            return False
        
    #si no encontro ningun divisor es primo
    return True


# Imprimir desde 4 hasta 1000
for i in range(4, 100):
    print(i, es_primo(i))



""""
print(2, True)
print(3, True)    
count =0
for i in range(4, 1000):
    if i % 2 == 0:
        print(i, False)
        
    elif i % 3 ==0 :
        print(i, False)
    
    elif i % 5 == 0:
        if i <= 5:
            print(i, True)
        else:
            print(i, False)
    elif i % 7 == 0:
        if i <= 7:
            print(i, True)
        else:
            print(i, False)
    elif i % 11 == 0:
        if i <= 11:
            print(i, True)
        else:
            print(i, False)
    else:
        print(i, True)
        count+=1
print(count)"""



