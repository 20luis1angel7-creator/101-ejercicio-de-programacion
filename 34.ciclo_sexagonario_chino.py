#  * Crea un función, que dado un año, indique el elemento 
#  * y animal correspondiente en el ciclo sexagenario del zodíaco chino.
#  * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
#  * - El ciclo sexagenario se corresponde con la combinación de los elementos
#  *   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
#  *   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
#  *   (en este orden).
#  * - Cada elemento se repite dos años seguidos.
#  * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).





def sexagenario(ano):
    elementos = ["madera", "fuego", "tierra", "metal", "agua"]
    animales = ["rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "oveja", 
                "mono", "gallo", "perro", "cerdo"]
    suma = ano - 1984
    
    print(elementos[suma // 2 % 5])
    print(animales[suma % 12])

sexagenario(2020)

















