from bs4 import BeautifulSoup
import requests

website = 'https://www.meteored.com.ar/tiempo-en_Viedma-America+Sur-Argentina-Rio+Negro-SAVV-1-16866.html'
           
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content,'lxml')
#print(soup.prettify())

box = soup.find('div',class_='flex-w')

title = soup.find('h1').get_text()

dia = box.find('span', class_='day').get_text()
#hora = box.find('span', class_='hour').get_text()
fecha = box.find('span', class_='subtitle-m').get_text()
temMax = box.find('span', class_='max changeUnitT').get_text()
temMin = box.find('span', class_='min changeUnitT').get_text()
print(title)
print(dia,fecha,"Temperatura máxima:", temMax,"Temperatura mínima:",temMin)





