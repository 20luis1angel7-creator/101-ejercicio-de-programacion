 # Escribe una función que reciba un texto y retorne verdadero o
 # falso (Boolean) según sean o no palíndromos.
 # Un Palíndromo es una palabra o expresión que es igual si se lee
 # de izquierda a derecha que de derecha a izquierda.
 # NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 # Ejemplo: Ana lleva al oso la avellana.

import re
import unicodedata

def es_palindromo(data):

    data_clear = re.sub(r"[^\w\s]", "", data) #investigue
    accent_clear = ''.join(c for c in unicodedata.normalize('NFD', data_clear) 
        if unicodedata.category(c) != 'Mn')#investigue
    
    text = accent_clear.replace(' ','').lower()
    
    invert = text[::-1]
    print(text)
    if text == invert:
        return True
    
    return False

print(es_palindromo("Ana lleva al oso la avellana"))


#inicio
#ingresar datos
#quitar los espacio, mayusculas (signo de puntuacion y tildes)
#invertir la cadena de texto
#comparar si es igual (invertida - normal)
#si es igual entonces
#es palindromo
#si no
#no es palindromo
#fin


















