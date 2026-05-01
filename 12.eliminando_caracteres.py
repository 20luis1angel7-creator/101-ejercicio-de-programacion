 # Crea una función que reciba dos cadenas como parámetro (str1, str2)
 # e imprima otras dos cadenas como salida (out1, out2).
 # - out1 contendrá todos los caracteres presentes en la str1 pero NO
 #   estén presentes en str2.
 # - out2 contendrá todos los caracteres presentes en la str2 pero NO
 #   estén presentes en str1.



#inicio
#ingresar datos
#separar los caracteres
#unir los 2 str eliminar los duplicados (compararla) 
# filtar
#fin


def eliminando_caracteres():
    str1 = "hola mundo"
    str2 = "hola python"

    outup1 = []
    outup2 = []
    out1 = ""
    out2 = ""

    for input_str1 in str1:
        if input_str1 not in str2:
            outup1.append(input_str1)
            #out1 = "".join(outup1)
            
    for input_str2 in str2:
        if input_str2 not in str1:
            outup2.append(input_str2)
            #out2 = "".join(outup2)
            
    out1 = "".join(outup1)
    out2 = "".join(outup2)

    return out1, out2

eliminando_caracteres()

print(eliminando_caracteres())









