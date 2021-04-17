# import libraries
import csv
import requests
from bs4 import BeautifulSoup

# all the pages
pages = [0, 30, 60 ,90, 120, 150, 180, 210, 240, 270, 300, 330, 360]

speechs_url = []

# loop over every page
for page in pages:
  url = f'https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/discursos?b_start:int={page}'
  print(f'sraping {url}')
  page = requests.get(url)
  soup = BeautifulSoup(page.content,"html.parser")
  # find all titles
  titles = soup.find_all('article', class_='tileItem')
  # get the url for each speech
  for title in titles:
    href = title.find('a', class_='summary url')['href']
    speechs_url.append(href)
    print(f'appending - {href} - to list')


# save speechs url to csv
with open('speechs_url.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(speechs_url)





