#  * Crea una función que calcule el valor del parámetro perdido
#  * correspondiente a la ley de Ohm.
#  * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
#  *   el valor del tercero (redondeado a 2 decimales).
#  * - Si los parámetros son incorrectos o insuficientes, la función retornará
#  *   la cadena de texto "Invalid values".




#inicio
#ingresar datos
#que sean 2, si es 1 o los 3 error
#verificar cuales son validos
# calcularlo
#retornar





def limpiar(valor):
    if valor != ""  :
        return valor
    try: 
        return float(valor)
    except:
        return None


def OHM(V, R, I):
    V,R,I = map(limpiar, (V,R,I))

    valores = [V,R,I]

    if valores.count(None) != 1:
        return "Invalid values"
  

    if V is None :
        V = I * R
        return round(V, 2)
    elif I is None:
        I = V / R
        if V == 0 or R == 0:
            return "Invalid values"
        return round(I, 2)
    elif R is None:
        R = V / I
        if V == 0 or I == 0:
            return "Invalid values"
        return round(R, 2)
    else:
        return "Invalid values"

print(OHM("",3,5))
