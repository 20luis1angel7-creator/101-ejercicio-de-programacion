#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet)
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")


#inicio
#introducir texto
#declarar numero y sus alfanumerico
#recorrer letra por letra
# intercanbiarlo por alfanumerico
# guardarlo
#retornar

import random 

def letras_a_hacker(letra):
    result = ""
    if letra == "a":
        result = random.choice(["4", "@", "^", "aye", "(L", "Д" ])
        return result
    elif letra == "b":
        result = random.choice(["I3", "8", "13", "|3", "ß", "!3", "(3", "/3", ")3", "|-]", "j3", "6" ])
        return result
    elif letra == "c":
        result = random.choice(["[", "¢", "{", "<", "(", "©" ])
        return result
    elif letra == "d":
        result = random.choice([")", "|)", "(|", "[)", "I>", "|>", "?", "T)", "I7", "cl", "|}", ">", "|]" ])
        return result
    elif letra == "e":
        result = random.choice(["3","&","£","€","ë","[-","|=-" ])
        return result
    elif letra == "f":
        result = random.choice(["|=","ƒ","|#","ph","/=","v" ])
        return result
    elif letra == "g":
        result = random.choice(["&","6","(_+","9","C-","gee","(?,","[,","{,","<-","(." ])
        return result
    elif letra == "h":
        result = random.choice(["#","/-/","[-]","]-[",")-(","(-)",":-:","|~|","|-|","]~[","}{","!-!","1-1","\\-/","I+I"])
        return result
    elif letra == "i":
        result = random.choice(["1","[]","|","!","eye","3y3","][" ])
        return result
    elif letra == "j":
        result = random.choice([",_|","_|","._|","._]","_]",",_]","]",";","1" ])
        return result
    elif letra == "k":
        result = random.choice([">|","|<","/<","1<","|c","|(","|{" ])
        return result
    elif letra == "l":
        result = random.choice(["1","£","7","|","|" ])
        return result
    elif letra == "m":
        result = random.choice(["JVI","[V]","[]V[]","|\\/|","^^","<\\/>","{V}","(v)","(V)","|V|","nn","IVI","]\\/[","1^1","ITI","JTI" ])
        return result
    elif letra == "n":
        result = random.choice(["^/","|\\|","/\\/","[\\]","<\\>","{\\}","|V","/V","И","^","ท" ])
        return result
    elif letra == "o":
        result = random.choice(["0","Q","()","oh","[]","p","<>","Ø" ])
        return result
    elif letra == "p":
        result = random.choice(["|*","|o","|º","?","|^","|>","9","[]D","|°","|7" ])
        return result
    elif letra == "q":
        result = random.choice(["(_,)","9","()","2","0","<|","&" ])
        return result
    elif letra == "r":
        result = random.choice(["I2", "|`", "|~", "|?", "/2", "|^", "lz", "|9", "2", "12", "®", "[z", "Я", ".-", "|2", "|-"])
        return result
    elif letra == "s":
        result = random.choice(["5", "$", "z", "§", "ehs", "es", "2"])
        return result
    elif letra == "t":
        result = random.choice(["7", "+", "-|-", "']['", "†", '"|"', "~|~"])
        return result
    elif letra == "u":
        result = random.choice(["(_)", "|_|", "v", "L|", "µ", "บ"])
        return result
    elif letra == "v":
        result = random.choice(["\\/", "|/", "\\|"])
        return result
    elif letra == "w":
        result = random.choice(["\\\\/\\\\/", "VV", "\\N", "'//", "\\\\'", "\\^/", "(n)", "\\V/", "\\X/", "\\|/", "\\_|_/", "\\_:_/", "Ш", "Щ", "uu", "2u", "\\\\\\/\\\\\\\\//", "พ", "v²"])
        return result
    elif letra == "x":
        result = random.choice(["><", "Ж", "}{", "ecks", "×", "?", ")(", "]["])
        return result
    elif letra == "y":
        result = random.choice(["j", "`/", "Ч", "7", "\\|/", "¥", "\\//"])
        return result
    elif letra == "z":
        result = random.choice(["2", "7_", "-/_", "%", ">_", "s", "~/_", "-\\_", "-|_"])
        return result
    else:
        return " "
    

    


def lenguaje_hacker():
    result = ""
    texto = "qwerty uiop asdfgh jklzx cvbnm"
    for i in texto:
        result += letras_a_hacker(i)
    print(result)

lenguaje_hacker()

# def lenguaje_hacker():
#     texto = "hOla como esta".lower()
#     reemplazar = {
#         "a": "4",
#         "b": "I3",
#         "c": "[",
#         "d": ")",
#         "e": "3",
#         "f": "|=",
#         "g": "&",
#         "h": "#",
#         "i": "1",
#         "j": ",_|",
#         "k": ">|",
#         "l": "1",
#         "m": "JVI",
#         "n": "^/",
#         "o": "0",
#         "p": "|*",
#         "q": "(_,)",
#         "r": "I2",
#         "s": "5",
#         "t": "7",
#         "u": "(_)",
#         "v": "|/",
#         "w": "VV",
#         "x": "><",
#         "y": "j",
#         "z": "2"
#     }

#     convertir = ""

#     for i in texto:
#         if i in reemplazar:
#             convertir += reemplazar[i]
#             print(convertir)
#         elif i == " ":
#             convertir += " "

# lenguaje_hacker()

