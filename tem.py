import requests
from bs4 import BeautifulSoup

## Primer paso debemos inspeccionar la pagina y el elemento que necesitamos extraer sus datos 
page=requests.get('https://www.meteored.com.py/tiempo-en_Shanghai-Asia-China-Shanghai-ZSPD-1-13494.html')
soup= BeautifulSoup(page.content,'html.parser')
actual= soup.find_all('span',class_=['dato-temperatura changeUnitT'])
actual=actual[0].get_text()
print ('Temperatura Actual en la ciudad de Changai: ',actual) # Imprimimos la temperatura actual de la ciudad elegida 
#obtenemos los datos que nos solicita el desafio 
maxima= soup.find_all('span',class_=['maxima changeUnitT'])
minima= soup.find_all('span',class_=['minima changeUnitT'])
viento= soup.find_all('span',class_=['velocidad'])
contador=0
#Identificamos el dia de hoy 
from datetime import datetime,date
dias=['Sunday','Monday','Tuesday', 'Wednesday','Thursday','Friday','Saturday']
hoy=datetime.today().strftime('%A')
contador=0
#Realizamos el recorrido de los proximos 7 dias.
print ('Pronóstico para los siguientes 7 días: ')
for item in maxima[0:6]:
    if contador==0:
        index= dias.index(hoy)
    max=str(maxima[contador].get_text())
    min=str((minima[contador].get_text()))
    vel=str((viento[contador].get_text()))
    datos=(' Temperatura maxima: '+item.get_text()+' Temperatura min: '+min + ' y la velocidad del viento entre: '+vel)
   
    print (dias[index]+datos)
    contador+=1
    index+=1
    if index==len(dias):
        index=0
