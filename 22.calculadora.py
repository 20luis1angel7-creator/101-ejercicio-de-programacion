#  * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
#  * resultado e imprímelo.
#  * - El .txt se corresponde con las entradas de una calculadora.
#  * - Cada línea tendrá un número o una operación representada por un
#  *   símbolo (alternando ambos).
#  * - Soporta números enteros y decimales.
#  * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
#  *   y división "/".
#  * - El resultado se muestra al finalizar la lectura de la última
#  *   línea (si el .txt es correcto).
#  * - Si el formato del .txt no es correcto, se indicará que no se han
#  *   podido resolver las operaciones.
#8h

#inicio
#leer el txt
#validar el orden
#validar si tiene letras, 3.2.1, etc
#si en el txt es igual a las operaciones +-*/
#sumar, multiplica, etc
#guardar el resultado
#mostrar resultados
#fin





with open("22challenge.txt", "r") as challenge:
    read_challenge = challenge.readlines() #guarda todas las lineas en una lista

    box1 = None
    box2 = None
    operator = None
    error = False
    expect_number = True #controla el orden correcto.  True → toca leer un número, False → toca leer un operador

    for read in read_challenge:
        read = read.strip() #strip(): elimina espacios y \n

        try:
            
            if read in "+-*/":
                if expect_number or operator is not None:
                    error = True
                    break
                operator = read
                expect_number = True
                continue
                
            num = float(read)

            if not expect_number:
                error = True
                break

            if box1 is None:
                box1 = num
            else:
                box2 = num

            expect_number = False
                
            if box1 is not None and box2 is not None and operator is not None:
                if operator == "+":
                    box1 = box1 + box2
                elif operator == "-":
                    box1 = box1 - box2
                elif operator == "*":
                    box1 = box1 * box2
                elif operator == "/":
                    box1 = box1 / box2
                
                box2 = None
                operator = None
                expect_number = False
         
        except ValueError:
            error = True
            break


    if operator is not None or error:
        print("error no se pudo completar el calculo")

    else:
        print("resultado final: ", box1)
















# with open("22challenge.txt", "r") as challenge:
#     read_challenge = challenge.readlines()

#     box1 = ""
#     box2 = ""
#     operator = ""

#     print(read_challenge)
#     for read in read_challenge:
#         try:
            
#             # print(read)
#             sinespacio = read.replace("\n","")
#             r = sinespacio.split(" ")
            
#             if read.strip() in "+-*/":
#                 operator = read
#             if "-" in r:
#                 operator = "-"
#             if "*" in r:
#                 operator = "*"
#             if "/" in r:
#                 operator = "/"

#             print(operator)

#             num=0
#             # box1 = r
            
#             readint = int(r[0])
#             if readint != "+-*/":
#                 box1 = read
#                 print(box1, "este")
            
#             if operator == "+":
#                 box2 = box1 + box2
#                 print(box2)


#             # elif num == 0:
#             #     box1.append(r)
#             #     print(box1, "q")
#             #     num +=1
#             # else:
#             #     box2.append(r)
#             #     print(box2, "h")
            
#             #if para sumar, restar, etc
            
#             # box1.append(r)
#             # print(box1)
#             # if box1 == "+":
#             #     print("h")
#             # else:
#             #     print("nada")

#         except ValueError:
#             print("ERROR")
        
        





















































