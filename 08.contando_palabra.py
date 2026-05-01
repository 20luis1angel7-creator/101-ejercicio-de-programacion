 # Crea un programa que cuente cuantas veces se repite cada palabra
 # y que muestre el recuento final de todas ellas.
 # - Los signos de puntuación no forman parte de la palabra.
 # - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 # - No se pueden utilizar funciones propias del lenguaje que
 #   lo resuelvan automáticamente.


#inicio
#insertar oracion
oracion = "domingo es el mejor domingo en el dia"
#leer las palabras y si se repite
separar = (oracion).split(" ")
#bucle palabras por palabras
contador = dict()
for i in separar:
    #si i esta dentro de contador             if....in.... (in)dentro
    if i in contador:
        #se suma 1 mas
        contador[i] += 1
    #si i no esta dentro de contador
    elif i not in contador:
        #sumale uno
        contador[i] = 1
    else:
        continue
print(contador)
