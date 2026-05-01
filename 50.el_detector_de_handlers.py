#  * Crea una función que sea capaz de detectar y retornar todos los
#  * handles de un texto usando solamente Expresiones Regulares.
#  * Debes crear una expresión regular para cada caso:
#  * - Handle usuario: Los que comienzan por "@"
#  * - Handle hashtag: Los que comienzan por "#"
#  * - Handle web: Los que comienzan por "www.", "http://", "https://"
#  *   y finalizan con un dominio (.com, .es...)


#inicio
#frase
#recorrer cada letra
#si comienza con @: guardamos 
#si empieza con #: guardamos
#si empieza con "www.", "http://", "https://"
# si termina con .com, .es: se guarda 
#se muestra todos los handler


def detector_de_handler():
    texto = "Hola @ana, mira esto: http://ejemplo.com #aprendizaje"
    letras = texto.split()
    handlers = []
    for l in letras:
        if "@" in l:
            # handlers.append(l)
            print(handlers)
        if "#" in l:
            # handlers.append(l)
            print(handlers)
        if "http://" in l or "www." in l or "https://" in l:
            if ".com" in l or ".es" in l:
                # handlers.append(l)
                print(handlers)

    return handlers

print(detector_de_handler())