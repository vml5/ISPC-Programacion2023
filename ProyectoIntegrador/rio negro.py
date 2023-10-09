import requests
from bs4 import BeautifulSoup

# URL de la página a raspar
url = 'https://www.meteored.com.ar/tiempo-en_Viedma-America+Sur-Argentina-Rio+Negro-SAVV-1-16866.html'

# Realizar una solicitud HTTP GET para obtener el contenido de la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido de la página con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar elementos que contienen la información que deseas
    # Por ejemplo, para obtener la temperatura actual:
    temperature = soup.find('span', class_='dato-temperatura').text

    # Para obtener la descripción del tiempo:
    description = soup.find('span', class_='estado').text

    # Para obtener la fecha y hora de la última actualización:
    last_updated = soup.find('span', class_='hora').text

    # Imprimir los resultados
    print('Temperatura actual:', temperature)
    print('Descripción del tiempo:', description)
    print('Última actualización:', last_updated)
else:
    print('La solicitud no fue exitosa. Código de estado:', response.status_code)
