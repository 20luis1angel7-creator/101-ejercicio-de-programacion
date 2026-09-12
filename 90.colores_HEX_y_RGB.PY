# /*
#  * Crea las funciones capaces de transformar colores HEX
#  * a RGB y viceversa.
#  * Ejemplos:
#  * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
#  * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
#  */

# numero = int("255")
# result = numero.str(16)
# print(result)

# base = int("80", 16)
# print(base)

def RGB(numRGB):
    # print(numRGB)

    R = numRGB[1:3]
    G = numRGB[3:5]
    B = numRGB[5:7]

    resultR = int(R, 16)
    resultG = int(G, 16)
    resultB = int(B, 16)
    return resultR, resultG, resultB

funcion_RGB = RGB("#FF5733")


def HEX(numHEX):
    listHex = numHEX.split(" ")
    num1 = listHex[0]
    num2 = listHex[1]
    num3 = listHex[2]
    conver1 = int(num1)
    conver2 = int(num2)
    conver3 = int(num3)
    # print(conver1, conver2, conver3)

    rgb1 = format(conver1, "02x")
    rgb2 = format(conver2, "02x")
    rgb3 = format(conver3, "02x")
    unir = "#" + "".join([rgb1, rgb2, rgb3]).upper()

    return unir

function_HEX = HEX("255 87 51")

print("HEX => RGB: ", funcion_RGB)
print("RGB => HEX: ", function_HEX)

