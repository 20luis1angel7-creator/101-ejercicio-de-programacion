 # Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 # de texto que representen fechas.
 # - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 # - La función recibirá dos String y retornará un Int.
 # - La diferencia en días será absoluta (no importa el orden de las fechas).
 # - Si una de las dos cadenas de texto no representa una fecha correcta se
 #   lanzará una excepción.



from datetime import timedelta, datetime
def how_many_days(getdate1, getdate2):
    try: 
        date1 = datetime.strptime(getdate1, "%d/%m/%Y")
        date2 = datetime.strptime(getdate2, "%d/%m/%Y")
        """date_day_first = date1.day
        date_day_second = date2.day"""

        ###(abs) lo convierte en positivo. (days) coge los dias###
        result = abs((date1 - date2).days)
    
        #out1 = date1 + timedelta(days=1)
        #out2 = date2 + timedelta(days=1)
        """result = date_day_first - date_day_second
        if result < 0:
            result -= result * 2"""
        return result
    except ValueError:
        return "error, the date format is invalid"
print(how_many_days("20/12/2025", "27/12/2025"))










