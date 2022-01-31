# write your code here
from collections import deque
import operator
import re


class UnknownVariable(Exception):
    def __str__(self):
        return "Unknown variable"


class InvalidIdentifier(Exception):
    def __str__(self):
        return "Invalid identifier"


class InvalidExpression(Exception):
    def __init__(self):
        pass


def is_valid_identifier(identifier):
    if not identifier.isalpha():
        raise InvalidIdentifier


class Calculator:
    def __init__(self):
        self.input = ''
        self.stack = deque()
        self.operators = {
            '+': {"precedence": 1, "function": operator.add},
            '-': {"precedence": 1, "function": operator.sub},
            '*': {"precedence": 2, "function": operator.mul},
            '/': {"precedence": 2, "function": operator.truediv},  # use operator.div for Python 2
            '^': {"precedence": 3, "function": operator.pow},
        }
        self.precedence_swap = 1
        self.symbols = list(self.operators.keys())
        self.variables = {}

    def is_variable_exist(self, variable):
        return variable in self.variables.keys()

    def fix_input(self):
        self.input = re.sub(r"\s\s+\s", " ", self.input)
        if re.search(r"\*\*+|//+|\^\^+", self.input):
            raise InvalidExpression

        self.input = re.sub(r"\++", "+", self.input)
        sub_pattern = r"--+"
        while True:
            match = re.search(sub_pattern, self.input)
            if not match:
                break

            end = match.end()
            symbol = '-' if (end - match.start()) % 2 else '+'
            new = re.sub(sub_pattern, symbol, self.input[:end])
            self.input = new + self.input[end:]

        symbols = self.symbols + ['(', ')']
        for symbol in symbols:
            self.input = self.input.replace(symbol, f' {symbol} ')

    def perform_assignment(self):
        variable, value = [operand.strip() for operand in self.input.split('=')]
        is_valid_identifier(variable)
        self.input = value
        self.postfix()
        value = self.perform_operation(self.stack)

        if value is not None:
            self.variables[variable] = value
        else:
            raise ValueError

    def get_actual_value(self, identifier):
        try:
            identifier = int(identifier)
        except ValueError:
            is_valid_identifier(identifier)
            if self.is_variable_exist(identifier):
                identifier = self.variables[identifier]
            else:
                raise UnknownVariable

        return identifier

    def place_digit(self, digit):
        digit = self.get_actual_value(digit)
        entities = [
            self.stack.pop()
            for _ in range(self.precedence_swap)
            if self.stack and self.stack[-1] in self.symbols
        ]

        self.stack.append(digit)
        for entity in reversed(entities):
            self.stack.append(entity)

    def place_symbol(self, symbol):
        entities = []
        self.precedence_swap = 1

        while True:
            if (
                not self.stack
                or self.stack[-1] not in self.symbols
                or self.operators[symbol]["precedence"]
                <= self.operators[self.stack[-1]]["precedence"]
            ):
                break
            self.precedence_swap += 1
            entities.append(self.stack.pop())

        self.stack.append(symbol)
        for entity in reversed(entities):
            self.stack.append(entity)

    def postfix(self):
        for entity in self.input.split():
            if entity in self.symbols:
                self.place_symbol(entity)
            elif entity == ')':
                sub_operations = []
                while True:
                    if self.stack and self.stack[-1] != '(':
                        sub_operations.append(self.stack.pop())
                    elif not self.stack:
                        raise InvalidExpression
                    else:
                        self.stack.pop()
                        break

                top_operator = ''
                value = self.perform_operation(reversed(sub_operations))
                if self.stack and self.stack[-1] in self.operators:
                    top_operator = self.stack.pop()

                self.stack.append(value)
                if top_operator:
                    self.stack.append(top_operator)
            elif entity == '(':
                self.stack.append(entity)
            else:
                self.place_digit(entity)

    def perform_operation(self, data_structure):
        stack = deque()
        try:
            for entity in data_structure:
                if entity in self.symbols:
                    operand_1 = stack.pop()
                    operand_2 = stack.pop()
                    stack.append(self.operators[entity]["function"](operand_2, operand_1))
                else:
                    stack.append(entity)
        except Exception:
            raise InvalidExpression

        return int(stack.pop())

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
                try:
                    if '=' in self.input:
                        self.perform_assignment()
                    else:
                        self.fix_input()
                        self.postfix()
                        print(self.perform_operation(self.stack))
                except ValueError:
                    print("Invalid assignment")
                except UnknownVariable as unknown:
                    print(unknown)
                except InvalidIdentifier as invalid:
                    print(invalid)
                except (KeyError, InvalidExpression):
                    print("Invalid expression")

                self.stack.clear()


calc = Calculator()
calc.main()
