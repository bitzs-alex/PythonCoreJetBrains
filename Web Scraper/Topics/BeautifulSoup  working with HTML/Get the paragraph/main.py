import requests

from bs4 import BeautifulSoup

search_word = input()
url = input()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
paragraphs = soup.find_all('p')

for paragraph in paragraphs:
    if search_word in paragraph.text:
        print(paragraph.text)
        break
