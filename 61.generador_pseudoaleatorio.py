#  * Crea un generador de números pseudoaleatorios entre 0 y 100.
#  * - No puedes usar ninguna función "random" (o semejante) del
#  *   lenguaje de programación seleccionado.
#  *
#  * Es más complicado de lo que parece...



def pseudoaleatorio():
    semilla = 42
    a = 1664525
    c = 1013904223
    m = 2**32

    x = semilla
    for _ in range(10):
        x = (a + x * c) % m
        mod = x % 100
        print(mod)
pseudoaleatorio()

