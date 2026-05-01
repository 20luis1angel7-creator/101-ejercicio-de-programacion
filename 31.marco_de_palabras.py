#  * Crea una función que reciba un texto y muestre cada palabra en una línea,
#  * formando un marco rectangular de asteriscos.
#  * - ¿Qué te parece el reto? Se vería así:
#  *   **********
#  *   * ¿Qué   *
#  *   * te     *
#  *   * parece *
#  *   * el     *
#  *   * reto?  *
#  *   **********


#inicio
#obtengo la oracion
# separo por letras
#cuento la cantidad de letra = n
#le aumento 1 o 2 mas
#para cada linea de n
#si esta en el inicio y final poner asterisco
#sino poner un aterisco al inicio de cada linea luego una palabra y luego otro aterisco
#hasta que se acaba las letras
#




def marco_de_palabras(texto):
    palabras = texto.split()

    max_len = max(len(p) for p in palabras)

    print("*" * (max_len + 4))

    for palabra in palabras:
        print("*", palabra.ljust(max_len) ,"*")

    print("*" * (max_len + 4))
























    # palabras = texto.split()

    # # Obtener la longitud de la palabra más larga
    # max_len = max(len(p) for p in palabras )
    
    # #linea superior
    # print("*" * (max_len + 4))

    # # # Palabras enmarcadas
    # for palabra in palabras:
    #     print("*", palabra.ljust(max_len), "*")

    # # #linea inferior
    # print("*" * (max_len+4))









    # separar = texto.split()
    # print(separar)

    # c = 0
    # for sep in separar:
    #     conteo = 0
        
    #     for _ in sep:
    #         conteo += 1
            
    #         if conteo > c:
    #             c = conteo
                
    #     print(c)
    
        
    # for i in range(c):
    #     for p in separar:
    #         if i == 0 or i == c -1:
    #             print("*" *c)
    #         else:
    #             print("*", p  , "*")


marco_de_palabras(texto = "hola que tal, hay dio mio que vaina")
