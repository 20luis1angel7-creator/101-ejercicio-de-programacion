#  * Crea una función que imprima los 30 próximos años bisiestos
#  * siguientes a uno dado.
#  * - Utiliza el menor número de líneas para resolver el ejercicio.
 


#inicio
# recibir el ano
#(while) mientras no haigan 30 anos bisiesto
#si es divisible por 4
#se guarda en una lista
#mostrar lista



def ano_bisiesto():

     


    year = int(input("digita tu ano: "))
    bisiesto = []
    while len(bisiesto) < 30:
        if (year % 4 == 0 and year % 100 != 0) or year% 400 == 0: 
            bisiesto.append(year)
        year += 1
    return bisiesto
print(ano_bisiesto())












# def ano_bisiesto():
#     year = int(input("escribe tu ano: "))
#     amount_year = []
#     amount = 0
#     while amount <= 30:
#         if year % 4 == 0:
#             amount_year.append(year)
#             amount += 1
#         year += 1
        
#     return amount_year

    
# print(ano_bisiesto())







