# import libraries
import os
import csv
import requests
from bs4 import BeautifulSoup

# create function to write to txt
def write_txt(filename):
  with open(filename, 'w') as writer:
    writer.write(title)
    writer.write(" ")
    writer.write(published)
    writer.write(" ")
    writer.write(text)


# get list of url
speechs_url = []

with open('speechs_url.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      speechs_url.append(row)

# scraping each speech
for url in speechs_url[0]:
  print(f'sraping {url}')
  url = url
  page = requests.get(url, verify=False)
  soup = BeautifulSoup(page.content,"html.parser")
  title = soup.find(id='main_ltTitulo').text
  date = soup.find(id='main_ltFEcha').text
  published  = f'Publicado em {date}'
  text = soup.find('div', class_='texto-bloque').text
  filename = date.replace(" ", "") + ".txt"
  print(f'{filename} saved')
  write_txt(filename)










