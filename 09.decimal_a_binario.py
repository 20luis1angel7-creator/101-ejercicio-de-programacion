 # Crea un programa se encargue de transformar un número
 # decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#5 H                    MEDIO                         ayuda de CHATGPT un 70%
#valor
numero = 13
#almacenador de datos
residuos = []
#bucle que hasta que numero no sea mayor que coro se siga ejecutando
while numero > 0:
    #los residuos forman el binario 13 % 2 = 1, 6 % 2 = 0 ,...
    residuo = numero % 2
    #guarda 
    residuos.append(residuo)
    #da el conciente entero 13 // 2 = 6, 6 // 2 = 3,...
    actualizar = numero // 2
    #para que e bucle no sea infinito
    numero = actualizar
#invertir 
binario = residuos[::-1]
print(binario)