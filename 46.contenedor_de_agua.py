#  * Dado un array de números enteros positivos, donde cada uno
#  * representa unidades de bloques apilados, debemos calcular cuantas unidades
#  * de agua quedarán atrapadas entre ellos.
#  *
#  * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
#  *
#  *         ⏹
#  *         ⏹
#  *   ⏹💧💧⏹
#  *   ⏹💧⏹⏹💧⏹
#  *   ⏹💧⏹⏹💧⏹
#  *   ⏹💧⏹⏹⏹⏹
#  *
#  *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
#  *   de agua. Suponemos que existe un suelo impermeable en la parte inferior
#  *   que retiene el agua.


#inicio
#para cada numero 



def rain_water(array):
    n = len(array)

    max_left = [0] * n
    max_right = [0] * n

    max_left[0] = array[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], array[i])

    max_right[n - 1] = array[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], array[i])

    water = 0
    for i in range(n):
        water += min(max_left[i], max_right[i]) - array[i]

    print(max_left, max_right, water)
rain_water([4,0,3,6,1,3])












































# def contenedor(array):
#     n = len(array)

#     max_left = [0] * n
#     max_right = [0] * n

#     max_left[0] = array[0]
#     for i in range(1, n):
#         max_left[i] = max(max_left[i - 1], array[i])

#     max_right[n - 1] = array[n - 1]
#     for j in range(n - 2, -1, -1):
#         max_right[j] = max(max_right[j + 1], array[j])

#     water = 0
#     for r in range(n):
#         water += min(max_left[r], max_right[r]) - array[r]

#     print(max_left, max_right, water)


        
# contenedor([4,0,3,6,1,3])





# 🧠 1. Problema clásico: “Trapping Rain Water”

# Busca este nombre tal cual:

# 👉 “Trapping Rain Water problem”

# Es un problema muy famoso en entrevistas técnicas. Hay varias formas de resolverlo, y entenderlas te dará mucha ventaja.

# 🧩 2. Idea fundamental del problema

# Debes comprender este concepto clave:

# 👉 El agua en una posición depende de los bloques más altos a la izquierda y a la derecha

# Es decir:

# No importa solo el valor actual
# Importa el máximo a la izquierda
# y el máximo a la derecha
# 📊 3. Prefijos y sufijos (muy importante)

# Investiga:

# “Prefix maximum array”
# “Suffix maximum array”

# Esto te enseña a:

# Guardar el máximo acumulado desde la izquierda
# Guardar el máximo acumulado desde la derecha

# Este es uno de los enfoques más comunes para resolverlo.

# 👉 4. Técnica de dos punteros (Two Pointers)

# Busca:

# 👉 “Two pointers technique”

# Y específicamente:
# 👉 “Trapping rain water two pointers solution”

# Esto es una versión más eficiente en memoria del problema.

# 🪟 5. Pensamiento de “nivel de agua”

# Debes entender esta idea mental:

# El agua se acumula hasta el mínimo entre los dos muros laterales
# Luego restas la altura del bloque actual

# Este concepto es CLAVE para no perderte.

# ⚡ 6. Complejidad algorítmica

# Investiga:

# O(n) vs O(n²)
# Cómo evitar recalcular cosas dentro de loops

# Tu solución inicial va por mal camino porque:
# 👉 estás pensando en “dibujar bloques”, no en calcular alturas

# 🧠 7. Visualización de problemas

# Este problema mejora mucho si entiendes:

# Cómo representar alturas como columnas
# Cómo imaginar “agua atrapada” entre picos

# Puedes buscar:
# 👉 “visual explanation trapping rain water”

# 🧱 8. Patrones relacionados

# Este problema mezcla varios patrones importantes:

# Arrays / listas
# Preprocesamiento
# Two pointers
# (opcional más avanzado) Stack (pila)
# 🎯 Resumen claro

# Para resolverlo por tu cuenta, enfócate en aprender:

# “Trapping Rain Water problem”
# Máximos a izquierda y derecha
# Prefix / suffix arrays
# Two pointers
# Complejidad O(n)
# Cómo calcular agua en cada posición