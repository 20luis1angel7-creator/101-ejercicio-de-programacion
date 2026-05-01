 # Escribe una función que calcule y retorne el factorial de un número dado
 # de forma recursiva.

#inicio
#ingresar el dato
#declara un duct
#mientras sea menor al dato ingresado
#se multiplica f x n = r
#se ingresa f = r
#se aumenta +1 a n
#ingresar n, agregar x
#mostrar resultado
#fin

def factorial_recursiva(n):
    #investigue
    if n == 0 or n == 1:
        return 1
    
    return  n * factorial_recursiva(n - 1)
    
print(factorial_recursiva(6))







'''number = 4
    n = 2
    f = 1
    while n <= number:
        r = f * n
        f = r
        n += 1
    return r'''
