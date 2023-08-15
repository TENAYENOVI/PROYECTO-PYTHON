import requests
from bs4 import BeautifulSoup

def obtener_contenido_pagina(url):
  response = requests.get(url)
  return response.text

def analizar_contenido_pagina(html):
  return BeautifulSoup(html, 'html.parser')

url = requests.get('https://diario.mx/')

soup = BeautifulSoup(url.content, 'html.parser')

titulos = []

titulo_items = soup.find_all('h2',class_='titulo_2')

titulo_items

for item in titulo_items:
  titulo=item.text.strip()
  titulos.append(titulo)

titulos

lugares = []
lugar_items = soup.find_all('small', class_='texto_3')

lugar_items

for item in lugar_items:
  lugar=item.text.strip()
  lugares.append(lugar)

lugares

notas = []
resumen_notas = soup.find_all('p', class_='texto_2')

resumen_notas

for item in resumen_notas:
  nota=item.text.strip()
  notas.append(nota)

notas

data = []
min_length = min(len(titulos), len(lugares), len(notas))

for i in range(min_length):
    data.append({
        "Título: ": titulos[i] if i < len(titulos) else None,
        "Lugares: ": lugares[i] if i < len(lugares) else None,
        "Noticia: ": notas[i] if i < len(notas) else None
    })

data

def procesar_pagina(soup):
  datos=[]

def manejar_paginacion(url_base, num_paginas):
    for i in range(1, num_paginas + 1):
        url = url_base + '/page-' + str(i) + ".html"  # Actualiza la URL base con el número de página actual
        contenido_pagina = obtener_contenido_pagina(url)
        soup = analizar_contenido_pagina(contenido_pagina)
        #procesar_pagina(soup)

url_base = "https://diario.mx/"
num_paginas = 10
manejar_paginacion(url_base, num_paginas)

data

len(data)

import pandas as pd
df = pd.DataFrame(data)

df

import datetime
fecha_actual = datetime.datetime.now().strftime("%d-%m-%y")

print(fecha_actual)
df.to_csv(f"../registro.json")

import datetime
fecha_actual = datetime.datetime.now().strftime("%d-%m-%y")

df.to_csv(f"Diario de Juarez-{fecha_actual}.csv", index=True)