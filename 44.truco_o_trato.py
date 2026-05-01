#  * Este es un reto especial por Halloween.
#  * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
#  * o Trato" y un listado (array) de personas con las siguientes propiedades:
#  * - Nombre de la niña o niño
#  * - Edad
#  * - Altura en centímetros
#  *
#  * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
#  * siguiendo estos criterios:
#  * - Un susto por cada 2 letras del nombre por persona
#  * - Dos sustos por cada edad que sea un número par
#  * - Tres sustos por cada 100 cm de altura entre todas las personas
#  * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
#  *
#  * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
#  * siguiendo estos criterios:
#  * - Un dulce por cada letra de nombre
#  * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
#  * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
#  * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
#  * - En caso contrario retornará un error.


# def truco_o_trato(evento, array):
#     cantidad_letra = 0
#     sum_altura = 0
#     sum_edades = 0
#     total = 0
#     lista = []

#     for n in array:
#         nombre = n[0]
#         cantidad_letra += len(nombre)
#         edad = n[1]
#         sum_edades += edad
#         altura = n[2]
#         sum_altura += altura
#     print(cantidad_letra, sum_edades, sum_altura)
    
#     if evento == "truco":
        
#         divicion_letras = round(cantidad_letra / 2)
#         divicion_edades = round(sum_edades / 2)
#         divicion_altura = round(sum_altura / 100)

#         emojis = ("🎃", "👻", "💀", "🕷", "🕸", "🦇")
#         total = divicion_edades + divicion_letras + divicion_altura

#         for e in range(total):
#             lista.append(emojis[e % 6])
#         return lista

#     elif evento == "trato":

#         for n in array:
#             edad = n[1]
#             if edad >= 10:
#                 anos = 3
#                 total += anos
#             elif edad < 10:
#                 anos = round(edad / 3)
#                 total += anos
                
#         dividir_altura = int(sum_altura / 50)

#         total_trato = dividir_altura + total + cantidad_letra

#         dulces = ("🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩")

#         lista = []
#         for i in range(1,total_trato + 1):
#             lista.append(dulces[i % 8])
#         return lista
    
#     else:
#         return "Error debe ser truco o trato"
        
# print(truco_o_trato("truco",(["maria", 6, 60], ["juancito", 12, 80])))



import random

def truco_o_trato(evento, array):
    resultado = []

    if evento == "truco":
        total = 0
        total_altura = 0

        for nombre, edad, altura in array:
            total = len(nombre) // 2

            if edad % 2 == 0:
                total += 2

            total_altura += altura

        total += total_altura // 100

        emojis = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]

        for _ in range(total):
            resultado.append(random.choice(emojis))

        return resultado
    
    elif evento == "trato":
        total = 0

        for nombre, edad, altura in array:
            total += len(nombre)

            edad_limite = min(edad, 10)
            total += edad_limite // 3

            altura_limite = min(altura, 150)
            total += (altura_limite // 50) * 2

        dulces = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]

        for _ in range(total):
            resultado.append(random.choice(dulces))

        return resultado
    
    else:
        return "Error: debe ser 'truco' o 'trato'"
    
print(truco_o_trato("trato",[["maria", 6,60], ["juancito", 12, 80]]))