 # Crea un programa que sea capaz de transformar texto natural a código
 # morse y viceversa.
 # - Debe detectar automáticamente de qué tipo se trata y realizar
 #   la conversión.
 # - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 #   o símbolos y dos espacios entre palabras "  ".
 # - El alfabeto morse soportado será el mostrado en
 #   https://es.wikipedia.org/wiki/Código_morse.


#letra a mrse
texto = "hola este texto va hacer codigo morse".lower()
cod_morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", 
             "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", 
             "7": "--...", "8": "---..", "9": "----.", "0": "-----", " ": "  "}
lista_morse=[]

#morse a letra
texto_morse = ".... --- .-.. .-"
cod_letras = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....":"h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", 
             "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", 
             "--...": "7", "---..": "8", "----.": "9", "-----": "0", "  ": " "}
lista_letras = []

for i in texto:   
    lista_morse.append(cod_morse[i])
morse = " ".join(lista_morse)    
print(morse) 

'''
for i in texto_morse:
    lista_letras.append(cod_letras[i])

print(lista_letras)
    
'''