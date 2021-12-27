import requests
import sys

from bs4 import BeautifulSoup

class Multilingual:
    def __init__(self):
        self.arguments = sys.argv
        self.word = self.arguments[3]
        self.request = requests.Session()
        self.translations = []
        self.example_contexts = []
        self.url = 'https://context.reverso.net/translation/{}-{}/{}'
        self.response = None
        self.unsupported_language = ''
        self.language_list = [
            'Arabic',
            'German',
            'English',
            'Spanish',
            'French',
            'Hebrew',
            'Japanese',
            'Dutch',
            'Polish',
            'Portuguese',
            'Romanian',
            'Russian',
            'Turkish',
        ]
        self.src_language = self.arguments[1]
        if self.language_list.count(self.src_language.capitalize()):
            self.src_language = self.language_list.index(self.src_language.capitalize())
        else:
            self.unsupported_language = self.src_language

        self.trg_language = self.arguments[2]
        if self.trg_language != 'all':
            if self.language_list.count(self.trg_language.capitalize()):
                self.trg_language = self.language_list.index(self.trg_language.capitalize())
            else:
                self.unsupported_language = self.trg_language

    def make_request(self):
        self.response = self.request.get(
            self.url.format(
                self.language_list[self.src_language].lower(),
                self.language_list[self.trg_language].lower(),
                self.word
            ),
            headers={'User-Agent': 'Mozilla/5.0'}
        )

        if self.response:
            return self.extract_translations()
        elif self.response.status_code == 404:
            print(f'Sorry, unable to find {self.word}')
        else:
            print('Something wrong with your internet connection')

        return False

    def extract_words(self, container):
        translations = container.find_all('a', {'class': 'translation'})

        for translation in translations:
            self.translations.append(translation.text.strip())

    def extract_example_contexts(self, container):
        examples = container.find_all('div', {'class': 'example'})

        for example in examples:
            source = example.find('div', {'class': 'src'})
            target = example.find('div', {'class': 'trg'})
            source_example = source.find('span', {'class': 'text'}).text.strip()
            target_example = target.find('span', {'class': 'text'}).text.strip()

            self.example_contexts.append([source_example, target_example])

    def extract_translations(self):
        soup = BeautifulSoup(self.response.content, 'html.parser')
        translations = soup.find('div', {'id': 'translations-content'})
        examples = soup.find('section', {'id': 'examples-content'})

        if translations and examples:
            self.extract_words(translations)
            self.extract_example_contexts(examples)
            return True

        return False

    def translation_results(self, size=5):
        target_language = self.language_list[self.trg_language]
        return f'{target_language} Translations:\n' + \
               '\n'.join(self.translations[:size]) + \
               f'\n\n{target_language} Examples:\n' + \
               '\n\n'.join(['\n'.join(src_trg) for src_trg in self.example_contexts[:size]])

    def translate_to_all(self):
        with open(self.word + '.txt', 'wb') as file:
            for key, lang in enumerate(self.language_list):
                self.trg_language = key

                if self.trg_language != self.src_language:
                    if not self.make_request():
                        break

                    result = '\n' + self.translation_results(1)
                    result += '\n' if lang != self.language_list[-1] else ''
                    file.write((result + '\n').encode())
                    print(result)
                    self.translations = []
                    self.example_contexts = []

    def main(self):
        if self.unsupported_language:
            print(f"Sorry, the program doesn't support {self.unsupported_language}")
        elif self.trg_language == 'all':
            self.translate_to_all()
        elif self.make_request():
            with open(self.word + '.txt', 'wb') as file:
                result = '\n' + self.translation_results()
                file.write((result + '\n').encode())
                print(result)


obj = Multilingual()
obj.main()
