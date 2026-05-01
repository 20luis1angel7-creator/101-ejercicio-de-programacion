#  * Crea un programa que calcule el daño de un ataque durante
#  * una batalla Pokémon.
#  * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
#  * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
#  * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
#  *   (buscar su efectividad)
#  * - El programa recibe los siguientes parámetros:
#  *  - Tipo del Pokémon atacante.
#  *  - Tipo del Pokémon defensor.
#  *  - Ataque: Entre 1 y 100.
#  *  - Defensa: Entre 1 y 100.


#inicio
#-ingresar datos
#-verificar que tipo de pokemos es
#hacer varios if 
#-realizar la formula


def batalla_pokemon():
    poke_atacante = input("ingresa el tipo poke atacante: ").lower()
    poke_defensor = input("ingresa el tipo poke defensa: ").lower()
    poke_ataque = int(input("ingresar el ataque: "))
    poke_defensa = int(input("ingresa defensa: "))

    if poke_ataque > 100 and poke_defensa > 100:
        return "el ataque y defensa debe ser menor que 100"

    if poke_atacante == "agua" and poke_defensor == "fuego":
        efectividad = 2
    elif poke_atacante == "fuego" and poke_defensor == "planta":
        efectividad = 2
    elif poke_atacante == "planta" and poke_defensor == "agua":
        efectividad = 2
    elif poke_atacante == "electrico" and poke_defensor == "agua":
        efectividad = 2
    elif poke_atacante == "fuego" and poke_defensor == "agua":
        efectividad = 0.5
    elif poke_atacante == "agua" and poke_defensor == "planta":
        efectividad = 0.5
    elif poke_atacante == "planta" and poke_defensor == "fuego":
        efectividad = 0.5
    elif poke_atacante == "electrico" and poke_defensor == "planta":
        efectividad = 0.5
    
    elif poke_atacante == "fuego" and poke_defensor == "electrico":
        efectividad = 1
    elif poke_atacante == "agua" and poke_defensor == "electrico":
        efectividad = 0.5
    elif poke_atacante == "planta" and poke_defensor == "electrico":
        efectividad = 0.5
    elif poke_atacante == "electrico" and poke_defensor == "fuego":
        efectividad = 1

    elif poke_atacante == poke_defensor:
        efectividad = 1
    else:
        return "Error that not found"
    


    #formula
    dano = int(50 * (poke_ataque / poke_defensa) * efectividad)
    return dano


print(batalla_pokemon())