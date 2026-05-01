 # Crea una función que reciba días, horas, minutos y segundos (como enteros)
 # y retorne su resultado en milisegundos.
#37 min

#inicio
#crear funcion
#ingresar dias, horas, min y seg (enteros)
#convertirlo a segundo cada uno
#sumarlo
#mostrar resultado



def dihomise():
    try:
        days = int(input("days: "))
        hours = int(input("hours: "))
        minute = int(input("minute: "))
        second = int(input("second: "))
    except ValueError:
        return "ERROR"
    ml_day = 86400000
    ml_hour = 3600000
    ml_minute = 60000
    ml_second = 1000 

    sume_ml_days = days * ml_day
    sume_ml_hour = hours * ml_hour
    sume_ml_minute = minute * ml_minute
    sume_ml_second = second * ml_second

    sume_total_ml = sume_ml_minute+sume_ml_hour+sume_ml_days+sume_ml_second

    print(sume_total_ml)

dihomise()






#sec: 1000 ml


