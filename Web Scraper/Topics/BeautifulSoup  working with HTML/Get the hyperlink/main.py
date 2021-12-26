import requests

from bs4 import BeautifulSoup

find_string = input()
url = input()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
anchors = soup.find_all('a')

for anchor in anchors:
    href_string = anchor.get('href')

    if find_string in href_string:
        print(href_string)
        break
