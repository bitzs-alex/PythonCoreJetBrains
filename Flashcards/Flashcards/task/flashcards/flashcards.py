# Write your code here
import argparse
import json
from io import StringIO
import random
import re


class FlashCard:
    def __init__(self):
        self.container = []
        self.choice = ""
        self.checked = []
        self.actions = ["add", "remove", "import", "export", "ask", "exit", "log", "hardest card", "reset stats"]
        self.logger = StringIO()
        self.export_path = ''

        argument_parser = argparse.ArgumentParser(description="Flash card Project")
        argument_parser.add_argument('--import_from', default=False, help="Path to import cards from")
        argument_parser.add_argument('--export_to', default=False, help="Path to export cards to")
        arguments = argument_parser.parse_args()

        if arguments.import_from:
            self.importer(arguments.import_from)
        if arguments.export_to:
            self.export_path = arguments.export_to

    def add_action(self):
        output = "The card:\n"
        term = input(output)
        self.log_writer(output, term + '\n')

        while True:
            if not self.get_actual_values(term):
                break

            output = f'The term "{term}" already exists. Try again:\n'
            term = input(output)
            self.log_writer(output, term + '\n')

        output = "The definition for card:\n"
        definition = input(output)
        self.log_writer(output, definition + '\n')

        while True:
            if not self.get_actual_values(definition, False):
                break

            output = f'The definition "{definition}" already exists. Try again:\n'
            definition = input(output)
            self.log_writer(output, definition + '\n')

        self.container.append({
            "term": term,
            "definition": definition,
            "mistake": 0
        })

        output = f'The pair ("{term}":"{definition}") has been added.'
        print(output)
        print(output, file=self.logger)

    def ask_action(self):
        while True:
            try:
                output = "How many times to ask?\n"
                count = int(input(output))
                self.log_writer(output, str(count) + '\n')
                break
            except ValueError:
                pass

        for _ in range(count):
            self.test()

    def exporter(self, file_name):
        with open(file_name, 'w') as file:
            counter = len(self.container)
            json.dump(self.container, file, indent=4)

        if counter:
            output = f"{counter} cards have been saved."
            print(output)
            print(output, file=self.logger)

    def export_action(self):
        output = "File name:\n"
        while True:
            file_name = input(output)
            self.log_writer(output, file_name + '\n')

            if re.match(r"\w+\.\w+", file_name):
                break

            output = "Wrong file name supplied. Inter file name with extension"
            print(output)
            print(output, file=self.logger)

        self.exporter(file_name)

    def get_actual_values(self, word, search_by_term=True):
        for card in self.container:
            term, definition, mistake = card.values()
            if (
                (search_by_term and word == term) or
                (not search_by_term and word == definition)
            ):
                return {
                    "term": term,
                    "definition": definition,
                }

        return None

    def hardest_card_action(self):
        if self.container:
            sorted_container = sorted(self.container, key=lambda card:card['mistake'], reverse=True)
            highest_mistake = sorted_container[0]['mistake']

            if highest_mistake:
                card_terms = []
                for card in sorted_container:
                    if card['mistake'] == highest_mistake:
                        card_terms.append(card['term'])
                    else:
                        break

                terms = '", "'.join(card_terms)
                output_1 = f'The hardest card {"are" if len(card_terms) > 1 else "is"} "{terms}".'
                output_2 = f'You have {highest_mistake} errors answering {"them" if len(card_terms) > 1 else "it"}.'
                print(output_1, output_2)
                print(output_1, output_2, file=self.logger)
                return

        output = "There are no cards with errors."
        print(output)
        print(output, file=self.logger)

    def importer(self, file_name):
        try:
            with open(file_name, 'r') as file:
                file_content = json.load(file)
        except FileNotFoundError:
            output = 'File not found.'
            print(output)
            print(output, file=self.logger)
        else:
            if file_content:
                for card in file_content:
                    term, definition, mistake = card.values()

                    if not self.get_actual_values(term):
                        self.container.append({
                            "term": term,
                            "definition": definition,
                            "mistake": mistake
                        })

                output = f"{len(file_content)} cards have been loaded."
                print(output)
                print(output, file=self.logger)

    def import_action(self):
        output = "File name:\n"
        file_name = input(output)
        self.log_writer(output, file_name + '\n')
        self.importer(file_name)

    def log_writer(self, *args):
        for arg in args:
            self.logger.write(arg)

    def log_action(self):
        output = "File name:\n"
        file_name = input(output)
        self.log_writer(output, file_name + '\n')

        with open(file_name, 'w') as log:
            for line in self.logger.getvalue():
                log.write(line)

            output = "The log has been saved."
            print(output)
            print(output, file=self.logger)

    def remove_action(self):
        output = "Which card?\n"
        term = input(output)
        self.log_writer(output, term + '\n')

        for index, card in enumerate(self.container):
            card_term = card['term']
            if card_term == term:
                self.container.pop(index)
                output = "The card has been removed."
                print(output)
                print(output, file=self.logger)
                return

        output = f'Can\'t remove "{term}": there is no such card.'
        print(output)
        print(output, file=self.logger)

    def reset_stats_action(self):
        for card in self.container:
            card['mistake'] = 0

        output = "Card statistics have been reset."
        print(output)
        print(output, file=self.logger)

    def test(self):
        while True:
            index = random.randint(0, len(self.container) - 1)
            term, definition, mistake = self.container[index].values()

            if term not in self.checked:
                self.checked.append(term)
                break
            elif len(self.checked) == len(self.container):
                break

        output = f'Print the definition of "{term}":\n'
        answer = input(output)
        self.log_writer(output, answer + '\n')
        if answer != definition:
            self.container[index]['mistake'] += 1
            correct_one = self.get_actual_values(answer, False)

            output = f'Wrong. The right answer is "{definition}"'
            output_1 = f', but your definition is correct for "{correct_one["term"]}"' if correct_one else ''
            print(output, output_1, '.', sep='')
            print(output, output_1, '.', sep='', file=self.logger)
        else:
            print('Correct!')
            print('Correct!', file=self.logger)

    def main(self):
        while self.choice != 'exit':
            while True:
                output = f"Input the action ({', '.join(self.actions)})\n"
                self.choice = input(output)
                self.log_writer(output, self.choice + '\n')

                if self.choice in self.actions:
                    break

                output = f"Wrong action choice. Only {', '.join(self.actions)} allowed.\n"
                print(output)
                print(output, file=self.logger)

            if self.choice != 'exit':
                self.choice = "_".join(self.choice.split())
                function = getattr(self, self.choice + '_action')
                function()
                print()
                print(file=self.logger)
            else:
                print("bye bye")
                print("bye bye", file=self.logger)

        if self.export_path:
            self.exporter(self.export_path)


flash_card = FlashCard()
flash_card.main()
