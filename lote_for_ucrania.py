import time
import requests
from bs4 import BeautifulSoup

    # Lote number from Elche
page_elche = requests.get('https://webparainmigrantes.com/extranjeria-elche-lote-nie/')
print(page_elche.status_code)

soup_elche = BeautifulSoup(page_elche.text, 'html.parser')
lote_number_elche = soup_elche.find_all('p')
print('ÚLTIMO LOTE NUMERO DE ELCHE ' + lote_number_elche[11].text)
print(lote_number_elche[12].text)

    # Lote number from Murcia
page_murcia = requests.get('https://webparainmigrantes.com/extranjeria-murcia-lote-nie/')
print(page_murcia.status_code)

soup_murcia = BeautifulSoup(page_murcia.text, 'html.parser')
lote_number_murcia = soup_murcia.find_all('p')
print('ÚLTIMO LOTE NUMERO DE MURCIA ' + lote_number_murcia[12].text)
print(lote_number_murcia[13].text)

    # Lote number from Alicante
page_alicante = requests.get('https://webparainmigrantes.com/tie-extranjeria-alicante-oficina-campo-de-mirra/')
print(page_alicante.status_code)

soup_alicante = BeautifulSoup(page_alicante.text, 'html.parser')
lote_number_alicante = soup_alicante.find_all('p')

print('ÚLTIMO LOTE NUMERO DE ALICANTE ' + lote_number_alicante[24].text)
print(lote_number_alicante[25].text)

#time.sleep(90000)
