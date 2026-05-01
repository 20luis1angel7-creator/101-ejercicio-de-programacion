 # Crea una función que evalúe si un/a atleta ha superado correctamente una
 # carrera de obstáculos.
 # - La función recibirá dos parámetros:
 #      - Un array que sólo puede contener String con las palabras
 #        "run" o "jump"
 #      - Un String que represente la pista y sólo puede contener "_" (suelo)
 #        o "|" (valla)
 # - La función imprimirá cómo ha finalizado la carrera:
 #      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 #        será correcto y no variará el símbolo de esa parte de la pista.
 #      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 #      - Si hace "run" en "|" (valla), se variará la pista por "/".
 # - La función retornará un Boolean que indique si ha superado la carrera.
 # Para ello tiene que realizar la opción correcta en cada tramo de la pista.
#3h 40m

def parametro():
    athlete = "run jump run" 
    athletics_track = "_ _ _"

    print("competence. ")
    
    separate = athlete.split(" ")
    sep_track = athletics_track.split(" ")

    save_athle_track = []
    valor = ""
    
    for i, e in zip(separate, sep_track):
        if i == "run" and e == "_" or i == "jump" and e == "|":
            save_athle_track.append(e)
            print(save_athle_track)
            
        elif i == "jump" and e == "_":
            save_athle_track.append("X")
            print(save_athle_track)
            valor = False
            
        elif i == "run" and e == "|":
            save_athle_track.append("/")
            print(save_athle_track)
            valor = False

        else:
            return False
    
    if (valor != False):
        print(save_athle_track)
        return True
    
    return False








    """
    if gano > 0 and brinco == 0 and choco == 0:
        print("gano cono")
        return True
    elif brinco > 0:
        print("noooo brincaste en pista")
        print("XXXXXXXXXXXXXXXXXXX")
        return False
    elif choco > 0:
        print("loco chocaste con la pared")
        print("////////////////////")
        return False
    else:
        return False"""


    """list_run = []
    list_track = []
    count_run = 0
    count_track = 0
    for e in separate:
        if e == "run":
            list_run += "1"
            count_run += 1
        else:
            list_run += "0"
    
    for e in sep_track:
        if e == "_":
            list_track += "1"
            count_track += 1
        else:
            list_track += "0"
    

    if count_run > count_track:
        print("//////////////")
        return False
    
    elif count_track > count_run:
            print("xxxxxxxxxxxxxxx")
            return False

    elif list_run == list_track:
        print("you have finished")
        print(athletics_track)
        return True
    
    else:
        return "error" """

parametro()

#run = 0
#jump = 1

#_ = 0
#| = 1

#si es 0 = 0
#si 1 = 1




















