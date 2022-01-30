import collections
import json
import re


class RiderBus:
    def __init__(self, json_string):
        self.errors = {}
        self.bus_data = json.loads(json_string)
        self.rules = {
            'bus_id': 0,
            'stop_id': 0,
            'stop_name': '',
            'next_stop': 0,
            'stop_type': '',
            'a_time': ''
        }

    def clear_errors(self, rules=()):
        self.errors = {}
        for key in rules:
            self.errors[key] = 0

    def type_requirement_errors(self):
        self.clear_errors(tuple(self.rules.keys()))

        for bus in self.bus_data:
            for key, value in bus.items():
                if type(value) == type(self.rules[key]):
                    if key == 'stop_type':
                        if len(value) > 1:
                            self.errors[key] += 1
                    elif self.rules[key] != 0 and not bool(value):
                        self.errors[key] += 1
                else:
                    self.errors[key] += 1

        self.display_errors("Type and required field")

    def format_errors(self):
        self.clear_errors(tuple(['stop_name', 'stop_type', 'a_time']))

        for bus in self.bus_data:
            for key, value in bus.items():
                if key == 'stop_name' and not re.match(r"^[A-Z].+?(Road|Avenue|Boulevard|Street)$", value):
                    self.errors[key] += 1
                elif key == 'stop_type' and value and not re.match(r"^[SOF]$", value):
                    self.errors[key] += 1
                elif key == 'a_time' and value and not re.match(r"^([01]\d|2[0-4]):([0-5]\d)$", value):
                    self.errors[key] += 1

        self.display_errors("Format")

    def display_errors(self, validation_type):
        total_errors = sum(self.errors.values())
        print(f'{validation_type} validation: {total_errors} errors')

        for key, value in self.errors.items():
            print(f"{key}: {value}")

    def

    def line_names(self):
        names_dict = collections.defaultdict(int)

        for bus in self.bus_data:
            names_dict[bus['bus_id']] += 1

        print('Line names and number of stops:')
        for bus_id, count in names_dict.items():
            print(f'bus_id: {bus_id}, stops: {count}')


json_string_input = input().strip()
rider = RiderBus(json_string_input)
# rider.type_requirement_errors()
# rider.format_errors()
rider.line_names()
