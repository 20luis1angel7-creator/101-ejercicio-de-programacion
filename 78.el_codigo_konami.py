#  * Crea un programa que detecte cuando el famoso "Código Konami" se ha
#  * introducido correctamente desde el teclado.
#  * Si sucede esto, debe notificarse mostrando un mensaje en la terminal.


#inicio
#lista teclado
#mientra cada una de la lista
# guardar cada tecla
# si sobrepasa los 10 eliminar el ultimo
#if codigo es igual a entrada

def el_codigo_konami():
    entrada = []
    codigo = [
    "UP",
    "UP",
    "DOWN",
    "DOWN",
    "LEFT",
    "RIGHT",
    "LEFT",
    "RIGHT",
    "B",
    "A"
    ]

    while True:
        en = input("tecla: ").upper()
        entrada.append(en)

        print(entrada)

        if en == '':
            print("sorry, we cant konami")
            break

        if entrada == codigo:
            print("!codigo konami")
            break

        if len(entrada) >= 10:
            entrada.pop(0)
el_codigo_konami()