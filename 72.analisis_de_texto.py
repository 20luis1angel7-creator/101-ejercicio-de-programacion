#  * Crea un programa que analice texto y obtenga:
#  * - Número total de palabras.
#  * - Longitud media de las palabras.
#  * - Número de oraciones del texto (cada vez que aparecen un punto).
#  * - Encuentre la palabra más larga.
#  *
#  * Todo esto utilizando un único bucle.


#inicio
#ingresar texto
#para cada palabra del texto:
# ir guardando la cantidad de letras (separado por " ")
# 
# guardar la cantidad de oraciones (si hay un . )
# contar la letras de cada parabra y coger la mas grande

def analisis_text():
    text = "La tecnología ha transformado la forma en que las personas se comunican, " \
    "trabajan y acceden a la información. Hace apenas unas décadas, enviar un mensaje a " \
    "alguien que vivía en otro país podía tomar días o incluso semanas. Hoy, gracias a " \
    "internet y a los dispositivos móviles, es posible conversar en tiempo real con " \
    "personas de cualquier parte del mundo."

    word_more_lenght = ""
    word = ""
    count = 0
    total_word = 0
    total_oracion = 0

    for letters in text:
        if letters == " ":
            total_word += 1
        
        if letters.isalpha():
            count += 1
            word += letters
        else:
            if len(word) > len(word_more_lenght):
                word_more_lenght = word
            
            word = ""

        if letters == ".":
            total_oracion += 1

    media = count / total_word
    
    print("media word: ", media)
    print("total word: ", total_word)
    print("total oracion: ", total_oracion) 
    print("word_more_lenght: ", word_more_lenght)
analisis_text()