import os
import requests
import string

from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        self.url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page='
        self.content = None
        self.articles = []
        self.pages = 0
        self.article_type = ''
        self.written_names = []

    def get_user_input(self):
        self.pages = int(input())
        self.article_type = input()

    def load_content(self, url):
        response = requests.get(url)

        if response:
            return (200, response.content)

        return (response.status_code, None)

    def write_to_file(self, name, content):
        with open(name, 'wb') as file:
            file.write(content.encode())

    def generate_file_name(self, title):
        punctuations = (string.punctuation).replace(' ', '') + '—'
        table = title.maketrans('', '', punctuations)
        title = title.translate(table)

        return title.replace(' ', '_').replace('__', '_') + '.txt'

    def find_articles(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        news_article_links = soup.find_all('span', {'class': 'c-meta__type'}, text=self.article_type)

        for news_article in news_article_links:
            anchor = news_article.find_parent('article').find('a', {'data-track-action': 'view article'})
            self.articles.append({
                'link': 'https://www.nature.com' + anchor.get('href'),
                'title': anchor.text
            })

    def get_article_body(self, content):
        soup = BeautifulSoup(content, 'html.parser')

        return soup.find('div', {'class': 'c-article-body'}).text

    def process_articles(self, counter):
        folder_name = 'Page_' + str(counter)
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)

        for article in self.articles:
            code, content = self.load_content(article['link'])

            if code == 200:
                name = self.generate_file_name(article['title'])
                name = os.path.join(folder_name, name)
                self.write_to_file(name, self.get_article_body(content))
                self.written_names.append(name)

    def main(self):
        self.get_user_input()
        counter = 1

        while counter <= self.pages:
            code, self.content = self.load_content(self.url + str(counter))

            if code == 200:
                self.find_articles()
                self.process_articles(counter)

            counter += 1

        if len(self.written_names):
            print('Saved all articles.')


scraper = Scraper()
scraper.main()
