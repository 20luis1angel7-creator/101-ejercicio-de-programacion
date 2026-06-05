#  * Crea una función que sea capaz de detectar si existe un viernes 13
#  * en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.


import calendar

def viernes_13():
    cal = calendar.monthcalendar(2026, 3)

    for semana in cal:
        if semana[calendar.FRIDAY] != 0 and semana[calendar.FRIDAY] == 13:
            print(semana[calendar.FRIDAY])
            return "True"
    
    return "False"

print(viernes_13())