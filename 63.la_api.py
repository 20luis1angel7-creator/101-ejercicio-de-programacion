#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs:
#  * https://github.com/public-apis/public-apis


import requests

# url = "https://api.thecatapi.com/v1/images/0XYvRd7oD"

# try:
#     res = requests.get(url)
    

#     print(res.status_code)
#     data = res.json()
#     print(data.keys())

#     # campos = list(data.keys())
#     print(data["id"])
#     print(data["url"])
#     print(data["breeds"])
#     print(data["width"])
# except requests.exceptions.RequestException as e:
#     print("error:", e)




url = " https://api.thecatapi.com/v1/images/search?limit=10"

try:
    res = requests.get(url)

    datas = res.json()
    
    for data in datas:
        print("id: ", data["id"])
        print("url: ", data["url"])
        print("width: ", data["width"])
        print("height: ", data["height"])
except requests.exceptions.RequestException as e:
    print("error:", e)