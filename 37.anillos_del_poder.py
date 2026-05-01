#  * ¡La Tierra Media está en guerra! En ella lucharán razas leales
#  * a Sauron contra otras bondadosas que no quieren que el mal reine
#  * sobre sus tierras.
#  * Cada raza tiene asociado un "valor" entre 1 y 5:
#  * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
#  *   Númenóreanos (4), Elfos (5)
#  * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
#  *   Huargos (3), Trolls (5)
#  * Crea un programa que calcule el resultado de la batalla entre
#  * los 2 tipos de ejércitos:
#  * - El resultado puede ser que gane el bien, el mal, o exista un empate.
#  *   Dependiendo de la suma del valor del ejército y el número de integrantes.
#  * - Cada ejército puede estar compuesto por un número de integrantes variable
#  *   de cada raza.
#  * - Tienes total libertad para modelar los datos del ejercicio.
#  * Ej: 1 Peloso pierde contra 1 Orco
#  *     2 Pelosos empatan contra 1 Orco
#  *     3 Pelosos ganan a 1 Orco


#inicio
#ingresar cantidades de los dos ejercito
#calcular por raza
#sumar por ejercito
#mostrar resultado



def calcular_poder(cantidadess, valores):
    total = 0
    for cantidad, valor in zip(cantidadess, valores):
        total += cantidad * valor
    return total

def batalla():
    print("los buenos") 
    buenos = [
        int(input("Pelosos: ")),
        int(input("Sureños buenos: ")),
        int(input("Enanos: ")),
        int(input("Númenóreanos: ")),
        int(input("Elfos: "))
    ]

    print("\nlos malos")
    mal = [
        int(input("Sureños malos: ")),
        int(input("Orcos: ")),
        int(input("Goblins: ")),
        int(input("Huargos: ")),
        int(input("Trolls: "))
    ]

    valores_bien = [1,2,3,4,5]
    valores_mal = [2,2,2,3,5]

    poder_bien = calcular_poder(buenos, valores_bien)
    poder_mal = calcular_poder(mal, valores_mal)

    print("\n poder del bien: ", poder_bien)
    print("poder del mal: ", poder_mal)

    if poder_bien > poder_mal:
        return f"ganador {poder_bien}"
    elif poder_mal > poder_bien:
        return f"ganador {poder_mal}"
    else:
        return "empate"
    
print(batalla())
    





# def anillo_del_poder():
#     print("los buenos")
#     c_pelosos = int(input("ingresa cantidad de pelosos: "))
#     c_surenos_buenos = int(input("ingresa cantidad de surenos buenos: "))
#     c_enanos = int(input("ingresar cantidad de enanos: "))
#     c_numeroreanos = int(input("ingresar cantidad de numeroreanos: "))
#     c_elfos = int(input("ingresar cantidad de elfos: "))

#     print("los malos")
#     c_surenos_malos = int(input("ingresa cantidad de surenos malos: "))
#     c_orcos = int(input("ingresa cantidad de orcos: "))
#     c_goblins = int(input("ingresar cantidad de goblins: "))
#     c_huargos = int(input("ingresar cantidad de huargos: "))
#     c_trolls = int(input("ingresar cantidad de trolls: "))

#     pelosos = c_pelosos * 1
#     surenos_buenos = c_surenos_buenos * 2
#     enanos = c_enanos * 3
#     numeroreanos = c_numeroreanos * 4
#     elfos = c_elfos * 5

#     surenos_malos = c_surenos_malos * 2
#     orcos = c_orcos * 2
#     goblins = c_goblins * 2
#     huargos = c_huargos * 3
#     trolls = c_trolls * 5

#     raza_bondadosa = pelosos + surenos_buenos + enanos + numeroreanos + elfos 
#     raza_malvadas = surenos_malos + orcos + goblins + huargos + trolls
#     print(raza_bondadosa, raza_malvadas)

#     if (raza_malvadas > raza_bondadosa):
#         return f"gano la raza malvada {raza_malvadas} a {raza_bondadosa}"
#     elif (raza_bondadosa > raza_malvadas):
#         return f"ganos la raza bondadosa {raza_bondadosa} a {raza_malvadas}"
#     else:
#         return f"hay un empate raza bondadosa {raza_bondadosa} y raza malvada {raza_malvadas}"

# print(anillo_del_poder())


