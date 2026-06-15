#  * ¡Estoy de celebración! He publicado mi primer libro:
#  * "Git y GitHub desde cero"
#  * - Papel: mouredev.com/libro-git
#  * - eBook: mouredev.com/ebook-git
#  *
#  * ¿Sabías que puedes leer información de Git y GitHub desde la gran
#  * mayoría de lenguajes de programación?
#  *
#  * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
#  * - Hash
#  * - Autor
#  * - Mensaje
#  * - Fecha y hora
#  *
#  * Ejemplo de salida:
#  * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.



import requests

url_repo = input("url del repo: ")

partes = url_repo.rstrip("/").split("/")

owner = partes[-2]
repo = partes[-1]

url_api = f"https://api.github.com/repos/{owner}/{repo}/commits"

response = requests.get(url_api)

if response.status_code == 200:
    for commit in response.json():
        print(f"Hash    : ", commit["sha"])
        print(f"Autor   : ", commit["commit"]["author"]["name"])
        print(f"Mensaje : ", commit["commit"]["message"])
        print(f"Fecha   : ", commit["commit"]["author"]["date"])
        print("-" * 80)
else:
    print("error: ", response.status_code)