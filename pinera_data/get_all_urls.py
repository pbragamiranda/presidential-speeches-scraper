# import libraries
import csv
import requests
from bs4 import BeautifulSoup

# all the pages
pages = range(1, 135)

speechs_url = []

# loop over every page
for page in pages:
  url = f'https://prensa.presidencia.cl/discursos.aspx?page={page}'
  print(f'sraping {url}')
  page = requests.get(url, verify=False)
  soup = BeautifulSoup(page.content,"html.parser")
  # find all the blocks
  bloques = soup.find_all('div', class_='bloque')
  # get the url for each speech
  for bloque in bloques:
      href = bloque.find('a', class_='btn')['href']
      full_url = f'https://prensa.presidencia.cl/{href}'
      speechs_url.append(full_url)
      print(f'appending - {full_url} - to list')
  # save speechs url to csv
  with open('speechs_url.csv', 'w') as myfile:
      wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
      wr.writerow(speechs_url)













