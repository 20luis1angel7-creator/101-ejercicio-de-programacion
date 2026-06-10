#  * Crea una función que sea capaz de transformar Español al lenguaje básico
#  * del universo Star Wars: el "Aurebesh".
#  * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
#  * - También tiene que ser capaz de traducir en sentido contrario.
#  *
#  * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
#  *
#  * ¡Que la fuerza os acompañe!

def aurebesh():
    frase = "¡Que la fuerza os acompañe!".lower()

    aurebesh = {
        "a": "aurek",
        "b": "besh",
        "c": "cresh",
        "d": "dorn",
        "e": "esk",
        "f": "forn",
        "g": "grek",
        "h": "herf",
        "i": "isk",
        "j": "jenth",
        "k": "krill",
        "l": "leth",
        "m": "mern",
        "n": "nern",
        "o": "osk",
        "p": "peth",
        "q": "qek",
        "r": "resh",
        "s": "senth",
        "t": "trill",
        "u": "usk",
        "v": "vev",
        "w": "wesk",
        "x": "xesh",
        "y": "yirt",
        "z": "zerek",
        " ": " ",
        "!": "!",
        "@": "@",
        "#": "#",
        "$": "$",
        "%": "%",
        "^": "^",
        "&": "&",
        "*": "*",
        "(": "(",
        ")": ")",
        "_": "_",
        "-": "-",
        "=": "=",
    }

    traducir = ""
    for i in frase:
        if i in aurebesh:
            traducir += aurebesh[i]
        
    print(traducir)
aurebesh()
