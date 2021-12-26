import requests

from bs4 import BeautifulSoup

url = input()
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
heading = soup.find('h1')

print(heading.text)
