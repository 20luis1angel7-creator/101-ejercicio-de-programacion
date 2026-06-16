#  * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
#  * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
#  *
#  * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
#  * del día 8. Mostrando hora e información de cada uno.
#  * Ejemplo: "16:00 | Bienvenida"
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.



import requests
from bs4 import BeautifulSoup

html = requests.get("https://holamundo.day").text
soup = BeautifulSoup(html, "html.parser")

for item in soup.select("span.rt-Text.rt-r-size-4"):
    hora = item.find("strong")

    if hora:
        hora_texto = hora.get_text(strip=True)

        texto = item.get_text(" ", strip=True)
        evento = texto.replace(hora_texto, "", 1).strip()

        print(f"{hora_texto} | {evento}")