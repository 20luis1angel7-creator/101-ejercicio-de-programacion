# /*
#  * Como cada año, el día 256 se celebra el "Día de la Programación".
#  * En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos
#  * 256 regalos para seguir aprendiendo programación:
#  * https://diadelaprogramacion.com
#  *
#  * Para seguir ayudando, te propongo este reto:
#  * Mostrar la sintaxis de los principales elementos de un lenguaje
#  * en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
#  *
#  * En un fichero, haz lo siguiente (si el lenguaje lo soporta),
#  * y comenta cada bloque para identificar con qué se corresponde:
#  * - Haz un "Hola, mundo!"
#  * - Crea variables de tipo String, numéricas (enteras y decimales)
#  *   y Booleanas (o cualquier tipo de dato primitivo).
#  * - Crea una constante.
#  * - Usa un if, else if y else.
#  * - Crea estructuras como un array, lista, tupla, set y diccionario.
#  * - Usa un for, foreach y un while.
#  * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
#  * - Crea una clase.
#  * - Muestra el control de excepciones.
#  *
#  * Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
#  * de sintaxis básica de muchos lenguajes.
#  *
#  * ¡Muchas gracias!
#  */

print("hola mundo")

letter = ""
number = 0
decimal = 0.0
boolean = True or False

APP = "mi aplicacion"
PI = 3.14159

if letter == "hola":
    print("como esta?")
elif letter == "klk":
    print("trankilo")
else:
    print("hola")

array = [1,2,3,4,5]
lista = {1,2,3,5,8}
tupla = ("manzana", "pera", "uva")
sett = set(1,2,6,3,8,2,5)
diccionario = {
    {1: "a"},
    {2: "b"},
    {3: "c"},
    {4: "d"}
}

n = 5
for i in range(n):
    print(i)

while i <= n:
    print(i)
    i + 1

def sumar(a, b):
    return a + b

class Persona:
    def __init__(self, nombre, carro):
        self.nombre = nombre
        self.carro = carro

    def tiene(seft):
        print("me llamo " + seft.nombre + "y tengo un " + seft.carro)

try: 
    numero = 8
    print(numero)
except ValueError:
    print("error") 