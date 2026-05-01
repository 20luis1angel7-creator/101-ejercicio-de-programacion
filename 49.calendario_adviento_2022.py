#  * ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
#  * 24 días, 24 regalos sorpresa relacionados con desarrollo de software,
#  * ciencia y tecnología desde el 1 de diciembre.
#  *
#  * Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
#  * lo siguiente:
#  * - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
#  *   de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
#  * - Si la fecha es anterior: Cuánto queda para que comience el calendario.
#  * - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
#  *
#  * Notas:
#  * - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
#  *   y finaliza a las 23:59:59.
#  * - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
#  *   y segundos.



#inicio
#obtener la fecha
#agregar una fecha de adviento inicio y fin
#agregar lista de sorteo
#si coincide esa fecha 
# fecha de cuando se termina el adviento
# devolver el regalo
#si la fecha es anterior 
# cuanto queda para que comience el calendario
#si es posterior
# cuanto tiempo ha pasado desde que ha finalizado



from datetime import datetime

def descomponer(td):
    dias = td.days
    return dias // 365, (dias % 365) // 30, (dias % 365) % 30

def calendario_adviento():
    fecha = datetime.strptime("27/10/2022 08:25:40", "%d/%m/%Y %H:%M:%S")
    fecha_inicio = datetime.strptime("01/12/2022 00:00:00", "%d/%m/%Y %H:%M:%S")
    fecha_fin = datetime.strptime("24/12/2022 23:59:59", "%d/%m/%Y %H:%M:%S")

    lista_regalos = [
        "casa", "nevera", "cama", "television", "carro", "libro de git", "libro de progamacion",
        "apartamento", "mueble", "estufa", "olla de presoin", "orno", "bicicleta", "laptop",
        "lavadora", "mesa gaming", "bono en comida", "a", "b", "resort", "s", "p","i","O"
    ]

    fin_del_dia = fecha.replace(hour=23, minute=59, second=59)
    hms = fin_del_dia - fecha

    if fecha_inicio <= fecha <= fecha_fin:
        regalo = lista_regalos[fecha.day - 1]
        print(regalo, hms)

    elif fecha > fecha_fin:
        td = fecha - fecha_fin
        ano, mes, dia = descomponer(td)
        print("es mayor")
        print(ano, "ano", mes, "mes", dia, "dia", hms)

    else:
        td = fecha_inicio - fecha
        ano, mes, dia = descomponer(td)
        print("es menor")
        print(ano, "ano", mes, "mes", dia, "dia", hms)


calendario_adviento()


# from datetime import datetime, timedelta

# def calendario_adviento():
#     fecha_texto = "27/10/2022 08:25:40"
#     fecha = datetime.strptime(fecha_texto, "%d/%m/%Y %H:%M:%S")
#     inicio_adviento = "01/12/2022 00:00:00"
#     fecha_inicio = datetime.strptime(inicio_adviento, "%d/%m/%Y %H:%M:%S")
#     fin_adviento = "24/12/2022 23:59:59"
#     fecha_fin = datetime.strptime(fin_adviento, "%d/%m/%Y %H:%M:%S")

#     fecha_dia = fecha.day
#     print(fecha)
    
#     lista_regalos = [
#         "casa", "nevera", "cama", "television", "carro", "libro de git", "libro de progamacion",
#         "apartamento", "mueble", "estufa", "olla de presoin", "orno", "bicicleta", "laptop",
#         "lavadora", "mesa gaming", "bono en comida", "a", "b", "resort", "s", "p","i","O"
#     ]
#     fin_del_dia = fecha.replace(hour=23, minute=59, second=59)
    
#     if fecha >= fecha_inicio and fecha <= fecha_fin:
#         # for i, v in enumerate(lista_regalos, 1):
#         #     if i == fecha_dia:
#         #         print(i, v)

#         regalo = lista_regalos[fecha.day - 1]
#         hms = fin_del_dia - fecha

#         print(regalo, hms)
#     elif fecha > fecha_fin:
#         print("es mayor")
        
#         hms = fin_del_dia - fecha
#         td = fecha - fecha_fin

#         ano = td.days // 365
#         mes = (td.days % 365) // 30
#         dia = (td.days % 365) % 30
        
#         print(ano,"ano", mes,"mes", dia,"dia", hms)
#     elif fecha < fecha_inicio:
#         print("es menor")
#         hms = fin_del_dia - fecha
#         td = fecha_inicio - fecha

        
#         print(ano,"ano", mes, "mes", dia,"dia", hms)

    
# calendario_adviento()