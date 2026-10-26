#  * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  * de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
#  * - Cada día que pasa:
#  *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#  *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
#  *     siguiente aumenta en un 20%.
#  *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
#  *     siguiente disminuya en un 20%.
#  *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
#  * - La función recibe el número de días de la predicción y muestra la temperatura
#  *   y si llueve durante todos esos días.
#  * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
#  */



import random

def clima_simulador(temp_inicial, proba_lluvia, cant_dias):
    temp_maxima = temp_inicial
    temp_minima = temp_inicial
    dias_lluvia = 0
    for i in range(cant_dias):
        print(f"dia {i}")
        cal = calcular(10) 
        if cal:
            print("true aumenta o disminuye 2 grados")
            if random.randint(1, 100) <= 50:
                temp_inicial += 2
                print("aumenta", temp_inicial)
            else:
                temp_inicial -= 2
                print("disminuye", temp_inicial)
        else:
            print("nada")

        if temp_inicial > 25:
            proba_lluvia += 20
        elif temp_minima < 5:
            proba_lluvia -= 20

        proba_lluvia = max(0, min(100, proba_lluvia))

        llueve = calcular(proba_lluvia)

        if llueve:
            dias_lluvia += 1
            print("esta lloviendo")
        else: 
            print("no esta lloviendo")

        print(f"Temperatura: {temp_inicial} °C")
        print(f"Probabilidad de lluvia: {proba_lluvia}%")

        temp_maxima = max(temp_maxima, temp_inicial)
        temp_minima = min(temp_minima, temp_inicial)

        if llueve:
            temp_inicial -= 1

        print("\n--- RESUMEN DE LA PREDICCIÓN ---")
        print(f"Temperatura máxima: {temp_maxima} °C")
        print(f"Temperatura mínima: {temp_minima} °C")
        print(f"Días con lluvia: {dias_lluvia}")

def calcular(i):
    n = random.randint(1, 100)
    if n <= i:
        return True
    else:
        return False

clima_simulador(20, 40, 20)











# 🧩 Pista 1: ¿Qué debe recibir tu función?

# Piensa en tres datos iniciales:
#     La temperatura inicial, por ejemplo, 20 °C.
#     La probabilidad inicial de lluvia, por ejemplo, 40 %.
#     La cantidad de días que quieres predecir, por ejemplo, 7 días.
# 🧩 Pista 2: ¿Para qué usarás los if?

# Exactamente, los if te servirán para comprobar las condiciones. Pero hay una diferencia entre comprobar una condición y generar un evento aleatorio.
# Por ejemplo:
#     Temperatura: cada día tienes un 10 % de posibilidades de que cambie 2 grados, hacia arriba o hacia abajo.
#     Temperatura superior a 25 °C: aumenta un 20 % la probabilidad de lluvia para el día siguiente.
#     Temperatura inferior a 5 °C: disminuye un 20 % la probabilidad de lluvia para el día siguiente.
#     Si llueve: la temperatura del día siguiente disminuye 1 grado.
# La clave es que necesitarás combinar condiciones (if) con números aleatorios para simular lo que sucede cada día.
# 🧩 Pista 3: ¿Cómo simularás los días?

# Piensa en un bucle que se repita tantas veces como días haya solicitado el usuario.
# En cada repetición tendrás que preguntarte:
#     ¿Cambia la temperatura hoy?
#     ¿Cuál es la probabilidad de lluvia de hoy?
#     ¿Llueve o no llueve hoy?
#     ¿Qué temperatura y probabilidad de lluvia habrá para mañana?
#     ¿Qué información debo mostrar de este día?
# Ojo: distingue entre la probabilidad de lluvia de hoy y la del día siguiente. Las reglas del enunciado hacen que algunas condiciones modifiquen la probabilidad para mañana.
# 🧩 Pista 4: ¿Cómo calcularás el resumen final?

# Además de mostrar el clima de cada día, necesitarás guardar tres datos mientras avanza la simulación:
#     Temperatura máxima: la más alta que hayas registrado.
#     Temperatura mínima: la más baja que hayas registrado.
#     Días de lluvia: un contador que aumente cada vez que llueva.