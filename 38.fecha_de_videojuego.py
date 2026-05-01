#  * ¡Han anunciado un nuevo "The Legend of Zelda"!
#  * Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
#  * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
#  * "The Legend of Zelda" de la historia?
#  * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
#  * que tú selecciones.
#  * - Debes buscar cada uno de los títulos y su día de lanzamiento 
#  *   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)



# The Legend of Zelda: Breath of the Wild  el 3 de marzo de 2017 
# The Legend of Zelda: Tears of the Kingdom 12 de mayo de 2023

from datetime import datetime

def comparar_fecha():
    # nombre_del_juego_1 = input("primer nombre del videojuego: ")
    # nombre_del_juego_2 = input("segundo nombre del videojuego: ")

    fecha_juego_1 = "2017-05-20" #input("primera fecha videojuego: ")
    fecha_juego_2 = "2020-03-29" #input("segunda fecha videojuego: ")

    fecha_1 = datetime.strptime(fecha_juego_1, "%Y-%m-%d")
    fecha_2 = datetime.strptime(fecha_juego_2, "%Y-%m-%d")

    total = fecha_2 - fecha_1
    print(total)

    anos = total.days // 365
    # print(anos)
    dias = total.days % 365
    # print(dias)

    print(f"cantidad de tiempo entre los juegos: {anos} anos y {dias} dias")
    

comparar_fecha()




















