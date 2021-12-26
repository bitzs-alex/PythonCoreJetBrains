class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars , cents):
        self.dollars = dollars
        self.cents = cents
        self.fix_numbers()

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        self.fix_numbers()

    def fix_numbers(self):
        while self.cents > 99:
            self.dollars += 1
            self.cents -= 100


class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # create methods here
    def __repr__(self):
        return f"Object of the class {__class__.__name__}. " \
               f"name: {self.name}, last_name: {self.last_name}, age: {self.age}"

    def __str__(self):
        return f"{self.name} {self.last_name}. {self.age}"
