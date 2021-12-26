import requests

from bs4 import BeautifulSoup

index = int(input())
url = input()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
sections = soup.find_all('h2')

print(sections[index].text)
