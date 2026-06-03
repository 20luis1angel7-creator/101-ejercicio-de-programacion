#  * Dada una URL con parámetros, crea una función que obtenga sus valores.
#  * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#  *
#  * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#  * los parámetros serían ["2023", "0"]
from urllib.parse import parse_qs, urlparse

def url_parametros():
    url = "https://retosdeprogramacion.com?year=2023&challenge=0"

    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    print(params)

    year = params["year"][0]
    challenge = params["challenge"][0]

    print(year)
    print(challenge)
    
url_parametros()