# write your code here
import operator
import re


def fix_operators(string):
    string = string.replace('+', '')
    string = string.replace('-', '1')
    return '-' if len(string) % 2 else '+'


class Calculator:
    def __init__(self):
        self.input = ''
        self.row_data = None
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,  # use operator.div for Python 2
        }

    def perform_operation(self):
        self.input = re.sub(r"\s\s+", " ", self.input)
        self.row_data = self.input.split()
        total = 0
        symbol = ''

        for key, entity in enumerate(self.row_data):
            if all(char in ['-', '+'] for char in entity):
                symbol = fix_operators(entity)
            else:
                try:
                    if key != 0:
                        total = self.operators[symbol](total, int(entity))
                    else:
                        total = int(entity)
                except (ValueError, KeyError):
                    print("Invalid expression")
                    return

        print(total)

    def main(self):
        while True:
            self.input = input().strip()

            if self.input == '/exit':
                print("Bye!")
                break
            elif self.input == '/help':
                print("The program calculates the sum and sub of numbers")
            elif self.input.startswith('/'):
                print("Unknown command")
            elif self.input:
                self.perform_operation()


calc = Calculator()
calc.main()
