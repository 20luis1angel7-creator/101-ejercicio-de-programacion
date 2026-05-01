 # Crea una función que reciba un String de cualquier tipo y se encargue de
 # poner en mayúscula la primera letra de cada palabra.
 # - No se pueden utilizar operaciones del lenguaje que
 #   lo resuelvan directamente.

def capital_letters(text):
    result = ""
    new_word = True

    for char in text:
        if char == " ":
            result += char
            new_word = True
        else:
            if new_word and "a" <= char <= "z":
                result += chr(ord(char) - 32)
                new_word = False
            else:
                result += char
                new_word = False

    return result


print(capital_letters("hola mundo como esta yo estoy muy bien"))

"""
def capital_letters():
    text = "hola mundo como esta yo estoy muy bien"
    words_save = []
    word = text.split()
    print(word)
    for w in word:
        cl = w.capitalize()
        words_save += cl
        print(words_save)
        textunido = "".join(words_save)
        print(textunido)
        if (textunido == "QWERTYUIOPASDFGHJKLZXCVBNM"):
            unido = " ".join(textunido)
            print(unido)
    
capital_letters()
"""













