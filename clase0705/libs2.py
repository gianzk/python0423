import requests # me sirve para conectarme al sitio web
from lxml import html # para extraer texto o navegar por el arbol html

url = 'https://www.wikipedia.org/'

# REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url)



parser = html.fromstring(respuesta.text)
idiomas = parser.find_class('central-featured-lang')

for idioma in idiomas:
    print(idioma.text_content())

