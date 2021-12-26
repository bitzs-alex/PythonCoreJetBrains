import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()
anchor_list = []
response = requests.get(url)

if response:
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find('div', {'id': 'PageContent_C002_Col00'})
    all_anchors = content_div.find_all('a')

    for anchor in all_anchors:
        if anchor.text and anchor.text[0] != letter:
            continue

        if anchor.text not in ['S', '']:
            anchor_list.append(anchor.text)

print(anchor_list)
