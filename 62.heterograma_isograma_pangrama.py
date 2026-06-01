#  * Crea 3 funciones, cada una encargada de detectar si una cadena de
#  * texto es un heterograma, un isograma o un pangrama.
#  * - Debes buscar la definición de cada uno de estos términos.

#inicio
#obtener la frase
#

def pangrama(texto):
    almacen = set([])
    letter = "aeiou"

    for i in texto:
        if i in letter:
            almacen.add(i)

    if len(almacen) != 5:
        return False
    
    return True

def heterograma(texto):
    almacen_heterograma = set([])

    for i in texto:
        almacen_heterograma.add(i)

    if len(almacen_heterograma) != len(texto):
        return False
            
    return True

def isograma(texto):
    almacen_iso = {}

    for letter in texto:
        if letter in almacen_iso:
            almacen_iso[letter] += 1
        else:
            almacen_iso[letter] = 1

    valores = list(almacen_iso.values())

    if len(set(valores)) == 1:
        return True
    
    return False


def pincipal():
    texto = "pangrmuieo"
    result = ""
    result += texto

    result += ": es pangrama," if pangrama(texto) else ": no es pangrama,"
    result += " es heterograma," if heterograma(texto) else " no es heterograma,"
    result += " es isograma" if isograma(texto) else " no es isograma"
    print(result)
        
    
pincipal()