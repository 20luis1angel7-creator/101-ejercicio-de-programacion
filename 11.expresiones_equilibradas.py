 # Crea un programa que comprueba si los paréntesis, llaves y corchetes
 # de una expresión están equilibrados.
 # - Equilibrado significa que estos delimitadores se abren y cieran
 #   en orden y de forma correcta.
 # - Paréntesis, llaves y corchetes son igual de prioritarios.
 #   No hay uno más importante que otro.
 # - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 # - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 


expresion1 = "{ [ a * ( c + d ) ] - 5 }"

# Símbolos de apertura y su correspondiente cierre
pares = {
    "(": ")",
    "{": "}",
    "[": "]"
}

simbolosApertura = pares.keys()
simbolosCierre = pares.values()

# Pila para almacenar los símbolos abiertos
pila = []

for i in expresion1:
    if i in simbolosApertura:
        # Si es un símbolo de apertura, lo guardamos en la pila
        pila.append(i)
    elif i in simbolosCierre:
        # Si es un símbolo de cierre, primero comprobamos si la pila no está vacía
        if not pila:
            print("Expresión NO balanceada: cierre sin apertura")
            break
        # Sacamos el último símbolo abierto
        ultimo = pila.pop()
        # Comprobamos si el cierre corresponde con la apertura
        if pares[ultimo] != i:
            print("Expresión NO balanceada: par incorrecto")
            break
else:
    # Si terminamos el bucle sin interrupciones, verificamos que la pila esté vacía
    if pila:
        print("Expresión NO balanceada: símbolos sin cerrar")
    else:
        print("Expresión balanceada")






        

"""
expresion1 = "{ [ a * ( c + d ) ] - 5 }"
simbolosApertura = "{(["
simbolosCierre = "})]"
pila = []

for i in expresion1:
    if i in simbolosApertura:
        pila.append(i)
        print(pila)
    if i in simbolosCierre:
        print(i)
        #if pila == simbolosApertura:
        ultimo = pila.pop()
        for "(" in ")" or "{" in "}" or "[" in "]":
            print(ultimo)
    if pila == []:
        print("desbalanceaada")

"""




   





#inicio
#ingresar los PLC
#para comprobar ir indice por indice
#almacenar los PLC que habren
#compararlo con los que cierran
#retornar true o false
#la pila quedo vacia o no






















