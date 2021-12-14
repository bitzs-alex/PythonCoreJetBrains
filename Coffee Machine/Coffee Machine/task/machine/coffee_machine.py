# Write your code here

# Base Class for all the Coffee Types
class Coffee:
    def __init__(self, name, required_water, required_beans, cost):
        self.name = name
        self.water = required_water
        self.beans = required_beans
        self.cost = cost


# To implement inheritance
class MilkedCoffee(Coffee):
    def __init__(self, name, required_watter, required_beans, cost, required_milk):
        # Calling the Parent constructor
        super().__init__(name, required_watter, required_beans, cost)
        self.milk = required_milk


class CoffeeMachine:
    def __init__(self):
        # NB: private attributes have two underscores in front of their name
        # Private attributes aren't meant to be accessed outside the current class

        # Available resources
        self.__resources = {
            'water':  400,
            'milk': 540,
            'coffee beans': 120,
            'disposable cups': 9,
        }

        self.__collected_money = 550

        # Storing all the coffee types our machine serve
        self.coffee_types = [
            Coffee('espresso', 250, 16, 4),
            MilkedCoffee('latte', 350, 20, 7, 75),
            MilkedCoffee('cappuccino', 200, 12, 6, 100)
        ]

    def withdraw_money(self):
        print(f'I gave you ${self.__collected_money}')
        self.__collected_money = 0

    def get_scarce_resource(self, chosen_coffee):
        if (
            isinstance(chosen_coffee, MilkedCoffee)
            and chosen_coffee.milk > self.__resources['milk']
        ):
            return 'milk'

        if chosen_coffee.water > self.__resources['water']:
            return 'water'

        if chosen_coffee.beans > self.__resources['coffee beans']:
            return 'coffee beans'

        return None

    def deduct_resources(self, chosen_coffee):
        if isinstance(chosen_coffee, MilkedCoffee):
            self.__resources['milk'] -= chosen_coffee.milk

        self.__resources['water'] -= chosen_coffee.water
        self.__resources['coffee beans'] -= chosen_coffee.beans
        self.__resources['disposable cups'] -= 1

    def make_coffee(self, chosen_coffee):
        scarce = self.get_scarce_resource(chosen_coffee)

        if scarce is None:
            print('I have enough resources, making you a coffee!')
            self.deduct_resources(chosen_coffee)
            self.__collected_money += chosen_coffee.cost
        else:
            print(f"Sorry, not enough {scarce}!")

    def resource_information(self):
        print('The coffee machine has:')

        for resource in self.__resources:
            print(f"{self.__resources[resource]} of {resource}")

        print(f"${self.__collected_money} of money")

    def fill_machine(self, resources):
        for resource in resources:
            self.__resources[resource] += resources[resource]

    def execute_action(self, action, choice=None, resources=None):
        if action == 'buy':
            self.make_coffee(choice)
        elif action == 'fill':
            self.fill_machine(resources)
        elif action == 'take':
            self.withdraw_money()
        elif action == 'remaining':
            self.resource_information()


def get_fillables():
    resources = {
        'water':  0,
        'milk': 0,
        'coffee beans': 0,
        'disposable cups': 0,
    }

    for resource in resources:
        if resource in ['milk', 'water']:
            measurement = 'ml of'
        elif resource == 'coffee beans':
            measurement = 'grams of'
        else:
            measurement = ''

        print(f'Write how many {measurement} {resource} you want to add:')
        resources[resource] = int(input().strip())

    return resources


def get_main_action():
    print('Write action (buy, fill, take, remaining, exit):')
    return input()


def get_coffee_type(machine):
    string = 'What do you want to buy?'
    coffees = machine.coffee_types

    for key, coffee in enumerate(coffees):
        string += f" {key + 1} - {coffee.name},"

    print(string + ' back - to main menu:')

    choice = input().strip()

    if choice == 'back':
        return None

    choice = int(choice) - 1
    return machine.coffee_types[choice]


def main():
    machine = CoffeeMachine()

    while True:
        action = get_main_action()

        if action == 'exit':
            break

        print()
        choice = None
        fillable = None

        if action == 'buy':
            choice = get_coffee_type(machine)

            if choice is None:
                print()
                continue
        elif action == 'fill':
            fillable = get_fillables()

        machine.execute_action(action, choice=choice, resources=fillable)

        print()


main()
