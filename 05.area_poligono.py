 # Crea una única función (importante que sólo sea una) que sea capaz
 # de calcular y retornar el área de un polígono.
 # - La función recibirá por parámetro sólo UN polígono a la vez.
 # - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 # - Imprime el cálculo del área de un polígono de cada tipo.
#30 M                              FACIL


def poligono():
    poli = input("que poligono desea calcular el area: ")

    if poli == "triangulo":
        base = int(input("cual es la base: "))
        altura = int(input("cual es la altura: "))
        area = (base * altura)/2
        return f"el area del triangulo es {area}"
    elif poli == "cuadrado":
        ancho = int(input("cual es la base: "))
        altura = int(input("cual es la altura: "))
        area = ancho * altura
        return f"el area del cuadrado es: {area}"
    elif poli == "rectangulo":
        ancho = int(input("cual es la base: "))
        altura = int(input("cual es la altura: "))
        area = ancho * altura
        return f"el area del rectangulo es {area}"
    else:
        return "hubo un error en algo... cheque donde fue...."

print(poligono())





