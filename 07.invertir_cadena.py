 # Crea un programa que invierta el orden de una cadena de texto
 # sin usar funciones propias del lenguaje que lo hagan de forma automática.
 # - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#30min                       FACIL
#ayuda de chatgpt ( estaba perdido en invertir la frase)

#cadena de texto
frase = "luis miguel"
#variable vacia para alamacenar los resultados
invertido = ""
#leer letra por letra
for invert in range(len(frase)):
    #invierte las letras
    invertido += frase[len(frase) - 1 - invert]
#mostrar
print(invertido)



