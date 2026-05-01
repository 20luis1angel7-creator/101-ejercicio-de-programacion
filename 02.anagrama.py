 # Escribe una función que reciba dos palabras (String) y retorne
 # verdadero o falso (Bool) según sean o no anagramas.
 # - Un Anagrama consiste en formar una palabra reordenando TODAS
 #   las letras de otra palabra inicial.
 # - NO hace falta comprobar que ambas palabras existan.
 # - Dos palabras exactamente iguales no son anagrama.
# 20:15s         MEDIO 

#anagrama es una palabra que tenga la misma letras peo en orden diferentes

#inicio
#ingresar las 2 palabras
#separar las letras
#ordenarla de forma alfabetica
#identificar si tienen las misma letras (es anagrama)
#si no (no es anagrama)


palabra1 = "luis"
palabra2 = "suli"

separar1 = list(palabra1)
separar2 = list(palabra2)

ordenar1 = sorted(separar1)
ordenar2 = sorted(separar2)


if ordenar1 == ordenar2:
    print("es anagrama")
elif ordenar1 != ordenar2:
    print("no es anagrama")
else:
    print("error")




