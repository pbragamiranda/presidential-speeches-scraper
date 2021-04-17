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
  page = requests.get(url)
  soup = BeautifulSoup(page.content,"html.parser")
  title = soup.find('h1', class_='documentFirstHeading').text
  print(title)
  date = soup.find("span", class_="value").text
  published  = f'Publicado em {date}'
  print(published)
  text = soup.find(id='parent-fieldname-text').text
  filename = date[:10].replace("/", "") + ".txt"
  print(filename)
  write_txt(filename)







