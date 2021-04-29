# import libraries
import csv
import uuid
import time
import os.path
import requests
from bs4 import BeautifulSoup

# create function to write to csv
def write_csv(filename):
  unique_filename = uuid.uuid4().hex + '___' + filename
  with open(f'csv_data/{unique_filename}', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    # writer.writerows(headers)
    writer.writerows(data)
    print(f'{unique_filename} created')

# get list of url
speechs_url = []

with open('speechs_url_2.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      speechs_url.append(row)


# scraping each speech
for url in speechs_url[0]:
  data = [['date', 'title', 'speech']]
  print(f'sraping {url}')
  url = url
  page = requests.get(url, verify=False)
  soup = BeautifulSoup(page.content,"html.parser")
  title = soup.find(id='main_ltTitulo').text
  date = soup.find(id='main_ltFEcha').text
  published  = f'Publicado em {date}'
  speech = soup.find('div', class_='texto-bloque').text
  filename = date[:10].replace("/", "") + ".csv"
  data.append([date, title, speech])
  write_csv(filename)
  time.sleep(10)











