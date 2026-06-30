#  * Crea un programa que realize el cifrado César de un texto y lo imprima.
#  * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
#  *
#  * Te recomiendo que busques información para conocer en profundidad cómo
#  * realizar el cifrado. Esto también forma parte del reto.


#inicio
#ingresar texto
#preguntar si es cifrar o descifrar
#para cada letra del texto:
# si es cifrar:
#  se suma 3 v a las posiciones del abecedario
# si es decifrar:
#  se restara 3 a las posiciones del abecedario
#mostrar

def cifrado_cesar():
    text = "cifrado y decifrado hecho"
    word = ""

    abc = [
        "a", "b", "c", "d", "e", "f", "g",
        "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z"
    ]
    ask = input("cifrado o decifrado: ")

    for c in text:
        if " " in c:
            word += " "
            continue
        else:
            position = abc.index(c)
        
        if ask == "cifrado":
            result = (position + 3) % 26
            word += abc[result]

        elif ask == "decifrado":
            result = (position - 3) % 26
            word += abc[result]

    print(word)

cifrado_cesar()