 # Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 # y retorne lo siguiente:
 # - "X" si han ganado las "X"
 # - "O" si han ganado los "O"
 # - "Empate" si ha habido un empate
 # - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 #   O si han ganado los 2.
 # Nota: La matriz puede no estar totalmente cubierta.
 # Se podría representar con un vacío "", por ejemplo.
 




def tres_en_raya():
    tabla = [["X", " ", "X"], 
             ["O" ,"X" ,"O"],
             ["X" ,"O" ," "]]
    countX=0
    countO=0
    for t in tabla:
        for e in t:
            if e == "X":
                countX+=1
            elif e == "O":
                countO+=1
  

    if countO > countX:
        return "NULL"
    
    hay_ganador= False
    
    #columnas
    if tabla[0][0]=="X" and tabla[1][0]=="X" and tabla[2][0]=="X":#[x,x,x]
        print("Gano X")
        hay_ganador= True
    elif tabla[0][0]=="O" and tabla[1][0]=="O" and tabla[2][0]=="O":
        print("Gano O")
        hay_ganador= True
    if tabla[0][1]=="X" and tabla[1][1]=="X" and tabla[2][1]=="X":#[x,x,x]
        print("Gano X")
        hay_ganador= True
    elif tabla[0][1]=="O" and tabla[1][1]=="O" and tabla[2][1]=="O":
        print("Gano O")
        hay_ganador= True
    if tabla[0][2]=="X" and tabla[1][2]=="X" and tabla[2][2]=="X":#[x,x,x]
        print("Gano X")
        hay_ganador= True
    elif tabla[0][2]=="O" and tabla[1][2]=="O" and tabla[2][2]=="O":
        print("Gano O")
        hay_ganador= True
    #fila
    if tabla[0][0]=="X" and tabla[0][1]=="X" and tabla[0][2]=="X":#[x][x][x]
        print("Gano X")
        hay_ganador= True
    elif tabla[0][0]=="O" and tabla[0][1]=="O" and tabla[0][2]=="O":
        print("Gano O")
        hay_ganador= True
    if tabla[1][0]=="X" and tabla[1][1]=="X" and tabla[1][2]=="X":#[x][x][x]
        print("Gano X")
        hay_ganador= True
    elif tabla[1][0]=="O" and tabla[1][1]=="O" and tabla[1][2]=="O":
        print("Gano O")
        hay_ganador = True
    if tabla[2][0]=="X" and tabla[2][1]=="X" and tabla[2][2]=="X":#[x][x][x]
        print("Gano X")
        hay_ganador= True
    elif tabla[2][0]=="O" and tabla[2][1]=="O" and tabla[2][2]=="O":
        print("Gano O")
        hay_ganador= True
    #diagonal (equis)
    if tabla[0][0]=="X" and tabla[1][1]=="X" and tabla[2][2]=="X":#[x][x][x]
        print("Gano X")
        hay_ganador= True
    elif tabla[0][0]=="O" and tabla[1][1]=="O" and tabla[2][2]=="O":
        print("Gano O")
        hay_ganador= True
    if tabla[0][2]=="X" and tabla[1][1]=="X" and tabla[2][0]=="X":#[x][x][x]
        print("Gano X")
        hay_ganador= True
    elif tabla[0][2]=="O" and tabla[1][1]=="O" and tabla[2][0]=="O":
        print("Gano O")
        hay_ganador= True

    if hay_ganador==False:
        print("empate")
#[abajo][lados]
    
tres_en_raya()





# def tres_en_raya():
#     tabla = [
#         ["X", " ", "X"],
#         ["O", "X", "O"],
#         ["X", "O", " "]
#     ]

#     # 1️⃣ Contar X y O
#     countX = 0
#     countO = 0
#     for fila in tabla:
#         for celda in fila:
#             if celda == "X":
#                 countX += 1
#             elif celda == "O":
#                 countO += 1

#     if countO > countX:
#         return "Nulo"

#     # 2️⃣ Todas las líneas posibles
#     lineas = []

#     # filas
#     lineas.extend(tabla)

#     # columnas
#     for c in range(3):
#         lineas.append([tabla[0][c], tabla[1][c], tabla[2][c]])

#     # diagonales
#     lineas.append([tabla[0][0], tabla[1][1], tabla[2][2]])
#     lineas.append([tabla[0][2], tabla[1][1], tabla[2][0]])

#     # 3️⃣ Revisar ganador
#     hay_x = False
#     hay_o = False

#     for linea in lineas:
#         if linea == ["X", "X", "X"]:
#             hay_x = True
#         if linea == ["O", "O", "O"]:
#             hay_o = True

#     if hay_x and hay_o:
#         return "Nulo"
#     if hay_x:
#         return "X"
#     if hay_o:
#         return "O"

#     return "Empate"






















  # for t in tabla[0]:
    #     if t == "X":
    #         countX+=1
    #     elif t == "O":
    #         countO+=1
    # for t in tabla[1]:
    #     if t == "X":
    #         countX+=1
    #     elif t == "O":
    #         countO+=1
    # for t in tabla[2]:
    #     if t == "X":
    #         countX+=1
    #     elif t == "O":
    #         countO+=1
  # for t in tabla[2]:
    #     print(t)
        # if t == "X":
        #     Xlen+=1
        # elif t == "O":
        #     Olen+=1

    # if tabla[0][0] == "X" or tabla[0][1] == "X" or tabla[0][2] == "X" or tabla[1][0] == "X" or tabla[1][1] == "X" or tabla[1][2] == "X" or tabla[2][0] == "X" or tabla[2][1] == "X" or tabla[2][2] == "X":
    #     countx+=1
        
    # if tabla[0][0] == "O" or tabla[0][1] == "O" or tabla[0][2] == "O" or tabla[1][0] == "O" or tabla[1][1] == "O" or tabla[1][2] == "O" or tabla[2][0] == "O" or tabla[2][1] == "O" or tabla[2][2] == "O":
    #     counto+=1
    
    
# if tabla[0] == ["X","X","X"] or tabla[1] == ["X","X","X"] or tabla[2] == ["X","X","X"] :
#         print("Gano las X")
#     elif tabla[0] == ["O", "O","O"] or tabla[1] == ["O", "O","O"] or tabla[2] == ["O", "O","O"]:
#         print("Gano las O")
#     elif tabla[0][0] == "X" and tabla[1][1] == "X" and tabla[2][2] == "X" or tabla[0][0] == "X" and tabla[1][1] == "X" and tabla[2][2] == "X":
#         print("Gano la X")
#     elif tabla[0][2] == "O" and tabla[1][1] == "O" and tabla[2][0] == "O" or tabla[0][2] == "O" and tabla[1][1] == "O" and tabla[2][0] == "O":
#         print("Gano las O")
#     else:
#         print("nooooo")
















