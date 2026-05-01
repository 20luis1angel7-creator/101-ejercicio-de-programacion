#  * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
#  * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.






def mcd(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


def mcm(a, b):
    return (a * b) // mcd(a, b)


print(mcd(12, 8))  # 4
print(mcm(4, 6))   # 12


#mcd: ej: 2 / 12 = 6, 3 /12 = 4 hasta llegar al 12. no vale 5 / 12 = 2.4, solo enteros
#inicio
#ingresar 2 numero
#n = num1
#for n = num1:
#se divide
#si se obtiene un numero entero se guarda
#aumentar n++

#mcm: ej: 4: 4X1=4, 4X2=8, 4X3=12 ....   se hace con los dos numero y el numero que sean iguales y mas pequeno ese es
#ingresar 2 nums
#num1
#loops num1 rango num1
#se multiplica
#se almacena el resultado
#loops num1 o otra num 2
#si son iguales
#se obtiene el resultado

# def mcd(a, b):
#     arraya = []
#     arrayb = []
#     resul1 = ""
#     aa =a
#     for a in range(aa):
#         a += 1
#         multia = aa / a
#         arraya.append(multia)
#         # print(arraya)
#     bb = b
#     for b in range(bb):
#         b += 1
#         multib = bb/b
#         arrayb.append(multib)
#         # print(arrayb)
    
#     for ab in arraya:
#         for ba in arrayb:
#             if ab == ba and ab > 3:
#                 resul1 = ab
                
#     return resul1
      
#     #pasarlo a entero

# print(mcd(12, 8))



# def mcm(a, b):
#     arraya = []
#     arrayb = []
#     resul = []
#     aa =a
#     for a in range(aa):
#         a += 1
#         multia = a * aa
#         arraya.append(multia)
        
#     bb = b
#     for b in range(bb):
#         b += 1
#         multib = b * bb
#         arrayb.append(multib)

#     for ab in arraya:
#         for ba in arrayb:
#             if ab == ba:
#                 resul.append(ab)
#     return resul
    
# print(mcm(4, 6))














