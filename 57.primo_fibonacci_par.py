#  * Escribe un programa que, dado un número, compruebe y muestre si es primo,
#  * fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

#inicio
#ingresar numero
#comprobar si es primo
#comprobar si es fibonacci
#comprobar si es impar
#mostrar resultado

def primo_fibonacci_par():
    numero = 13

    #primo
    es_primo = True

    if numero < 2:
        es_primo = False
    else:
        for i in range(2, numero):
            if numero % 1 == 0:
                es_primo = False
                break

    # fibonacci   
    a, b = 0, 1
    es_fibonacci = False

    while a <= numero:
        if a == numero:
            es_fibonacci = True
            break
        a, b = b, a + b

    #par
    es_par = numero % 2 == 0

    #resultado
    resultado = f"{numero}"

    resultado += ": es primo, " if es_primo else ": no es primo, "
    resultado += "es fibonacci y " if es_fibonacci else "no es fibonacci y "
    resultado += "es par" if es_par else "es impar" 

    print(resultado)        
primo_fibonacci_par()





# def primo_fibonacci_par():
#     numero = 13

#     suma = 0
#     #primo
    
#     for i in range(numero, 1, -1):
#         if i % 2 == 0:
#             continue
#         divi = numero / i 
#         if divi == 1 or divi == numero:
#             suma += 1
#     if suma == 1 or numero == 2:
#         print("es primo")
#     else:
#         print("no es primo")



#     #fibonacci
#     n = 0
#     n2 = 1
#     n3 = 0
#     fibonacci = []
#     for i in range(numero):
#         n3 = n + n2
#         fibonacci.append(n3)
#         n2 = n
#         n = n3

#     if numero in fibonacci:
#         print("es fibonacci")
#     else:
#         print("no es fibonacci")
     
#     #par
#     if numero % 2 == 0:
#         print("es par")
#     else:
#         print("es impar")
    
# primo_fibonacci_par()


