#Nombre: Jesús Ponce de León Mota
#Matrícula: 1850070
import requests
import csv
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")
frases_html = html.find_all("span", class_="text")
autores_html = html.find_all("small", class_="author")

frases = list()
for frase in frases_html:
    frases.append(frase.text)
autores = list()
for autor in autores_html:
    autores.append(autor.text)

for x in zip(frases, autores):
    print(x)

with open("./citas_1850070.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, dialect="excel")
    csv_writer.writerows(zip(frases, autores))

print("20/03/2023")

