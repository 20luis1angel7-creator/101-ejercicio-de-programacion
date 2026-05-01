 # Escribe una función que calcule si un número dado es un número de Armstrong
 # (o también llamado narcisista).
 # Si no conoces qué es un número de Armstrong, debes buscar información
 # al respecto.




def armstrong(n):
    if type(n) == str:
        return "no puede ser str"
    if n < 0:
        return "no se puede con digitos menores que 0"
    else:
        convert = str(n)
        long = len(convert)
        accumulator = 0
        for div in convert:
            intDiv = int(div)
            intDiv **= long
            accumulator += intDiv
            
        if accumulator == n:
            return True
        else:
            return False
        
print(armstrong(153))






'''def armstrong(n):
    str(n)
    separar = n.split('')
    print(separar)
    stack = 0
    for div in n:
        intDiv = int(div)
        print(intDiv)
        intDiv **= 3
        stack += intDiv
        
    if stack == n:
        return "es armstrong"
    else:
        print(stack)
        return "no es armstrong"

print(armstrong(153))'''

