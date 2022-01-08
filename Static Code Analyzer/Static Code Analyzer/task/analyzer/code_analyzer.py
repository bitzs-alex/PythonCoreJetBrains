from os import path, walk

import ast
import sys
import re


def is_not_snake_case(variable):
    return bool(re.search(r'[A-Z]', variable))


class Analyzer:
    def __init__(self):
        self.path = sys.argv[1]
        self.current_line = ''
        self.counter = 0
        self.semicolon = ';'
        self.hash = '#'
        self.construction = ''
        self.current_file_path = ''
        self.file_content = []
        self.max_4_lines = []
        self.multiple_line_found = False
        self.current_tab_size = 0
        self.function_tab_size = 0
        self.inside_function = False

    def path_walker(self, location):
        for dir_path, dir_name, filenames in walk(location):
            for file_name in filenames:
                self.current_file_path = path.join(location, file_name)

                if path.isdir(self.current_file_path):
                    print('am not here')
                    self.path_walker(self.current_file_path)
                else:
                    split_name = path.splitext(self.current_file_path)

                    if split_name[1] == '.py':
                        self.process_file()

    def process_file(self):
        self.current_line = ''
        self.counter = 0
        self.file_content = []
        self.max_4_lines = []
        self.multiple_line_found = False

        try:
            with open(self.current_file_path) as reader:
                self.file_content = reader.readlines()
        except FileNotFoundError:
            print('File Not found in specified location')
        else:
            for self.current_line in self.file_content:
                self.counter += 1

                self.max_4_lines.append(self.current_line)

                if len(self.max_4_lines) > 4:
                    self.max_4_lines.pop(0)

                self.check_errors()

    def check_errors(self):
        self.s001()
        self.s002()
        self.s003()
        self.s004()
        self.s005()
        self.s006()

        self.current_line = self.current_line.strip()
        self.get_construction()
        if self.construction:
            self.s007()

            if self.construction == 'class':
                self.s008()
            else:
                self.check_function()

            self.construction = ''
        elif self.inside_function:
            self.s011()

        if self.current_tab_size < self.function_tab_size:
            self.inside_function = False
            self.function_tab_size = 0

    def check_function(self):
        if not self.inside_function:
            self.inside_function = True
            self.function_tab_size = self.current_tab_size

        self.s009()
        definition = self.current_line[:re.search(r"\)[\w\s\->]*?:", self.current_line).end()]
        function = ast.parse(definition + 'pass').body[0]
        self.s010(function)
        self.s012(function)

    def s001(self):
        if len(self.current_line) > 79:
            print(f"{self.current_file_path}: Line {self.counter}: S001 Too long")

    def s002(self):
        self.current_tab_size = 0
        start_with_space = self.current_line.startswith(' ')

        if start_with_space:
            for char in self.current_line:
                if char != ' ':
                    break

                self.current_tab_size += 1

            if self.current_tab_size % 4 != 0:
                print(f"{self.current_file_path}: Line {self.counter}: "
                      f"S002 Indentation is not a multiple of four")

    def s003(self):
        semicolon_index = self.current_line.find(self.semicolon)

        if semicolon_index != -1 and self.check_misplacement(semicolon_index):
            print(f"{self.current_file_path}: Line {self.counter}: "
                  f"S003 Unnecessary semicolon")

    def check_misplacement(self, index):
        substring = self.current_line[:index]

        def check_quote_error(quote):
            split_list = self.current_line.split(quote)
            list_length = len(split_list)

            if list_length >= 2 and split_list[1].find(self.semicolon) == -1:
                return True

            return True if list_length == 1 else False

        return (self.hash not in substring) and check_quote_error("'") and check_quote_error('"')

    def s004(self):
        hash_index = self.current_line.find(self.hash)

        if hash_index != -1 and not self.current_line.startswith(self.hash):
            sub_str = self.current_line[:hash_index]

            if not sub_str.endswith('  '):
                print(f"{self.current_file_path}: Line {self.counter}: "
                      f"S004 At least two spaces required before inline comments")

    def s005(self):
        todo_found = self.current_line.lower().find('todo')

        if todo_found != -1 and self.hash in self.current_line[:todo_found]:
            print(f"{self.current_file_path}: Line {self.counter}: S005 TODO found")

    def s006(self):
        if (not self.multiple_line_found) and self.current_line.strip() and self.all_lines_empty():
            self.multiple_line_found = True
            print(f"{self.current_file_path}: Line {self.counter}: "
                  f"S006 More than two blank lines used before this line")

    def s007(self):
        if re.match(self.construction + r'\s\s', self.current_line):
            print(f"{self.current_file_path}: Line {self.counter}: "
                  f"S007 Too many spaces after '{self.construction}'")

    def s008(self):
        class_name = self.current_line[len(self.construction):].strip()
        match = re.match(r'\w+?[\s:(]', class_name)

        if match:
            class_name = class_name[:match.end() - 1]

            if re.match(r'^[a-z_]+$', class_name):
                print(f"{self.current_file_path}: Line {self.counter}: "
                      f"S008 Class name '{class_name}' should use CamelCase")

    def s009(self):
        func_name = self.current_line[len(self.construction):].strip()
        match = re.match(r'\w+?[\s:(]', func_name)

        if match:
            func_name = func_name[:match.end() - 1]

            if is_not_snake_case(func_name):
                print(f"{self.current_file_path}: Line {self.counter}: "
                      f"S009 Function name '{func_name}' should use snake_case")

    def s010(self, function):
        for arg in function.args.args:
            if is_not_snake_case(arg.arg):
                print(f"{self.current_file_path}: Line {self.counter}: "
                      f"S010 Argument name '{arg.arg}' should be snake_case")

    def s011(self):
        expression = ast.parse(self.current_line).body

        if expression and type(expression[0]) == ast.Assign:
            variable_name = self.current_line[:re.search(r'[/*+\-%]*?\s*?=\s*?', self.current_line).start()].strip()

            if is_not_snake_case(variable_name):
                print(f"{self.current_file_path}: Line {self.counter}: "
                      f"S011 Variable '{variable_name}' in function should be snake_case")

    def s012(self, function):
        for default in function.args.defaults:
            typ = type(default)
            if typ in [ast.List, ast.Dict, ast.Set]:
                print(f"{self.current_file_path}: Line {self.counter}: "
                      f"S012 Default argument value is mutable")

    def get_construction(self):
        if re.match(r'class\s', self.current_line):
            self.construction = 'class'
        elif re.match(r'def\s', self.current_line):
            self.construction = 'def'

    def all_lines_empty(self):
        empty_lines = list(filter(lambda line: len(line.strip()) == 0, self.max_4_lines))
        return len(empty_lines) > 2

    def run(self):
        if path.isdir(self.path):
            self.path_walker(self.path)
        else:
            self.current_file_path = self.path
            self.process_file()


if __name__ == '__main__':
    analyze = Analyzer()
    analyze.run()
