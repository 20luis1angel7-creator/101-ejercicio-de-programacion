#  * Crea una función que sume 2 números y retorne su resultado pasados
#  * unos segundos.
#  * - Recibirá por parámetros los 2 números a sumar y los segundos que
#  *   debe tardar en finalizar su ejecución.
#  * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
#  *   asíncrona, es decir, sin detener la ejecución del programa principal.
#  *   Se podría ejecutar varias veces al mismo tiempo.
#  


#inicio
#ingresar 2n, y los seg
#retraso de seg
#suma
#devolver resultado
#fin


import asyncio

async def parando_el_tiempo(n1, n2, sec):
    numberOne = n1
    numberTwo = n2
    second = sec

    await asyncio.sleep(second) 
    
    return numberOne + numberTwo

result = asyncio.run(parando_el_tiempo(4, 4, 2))
print(result)

























# Inicio
# Recibir números y segundos
# Iniciar espera sin bloquear
# Pasado el tiempo:
# calcular la suma
# entregar el resultado
# Fin