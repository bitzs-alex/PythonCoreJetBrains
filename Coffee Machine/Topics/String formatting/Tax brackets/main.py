gross = int(input().strip())


class Tax:
    def __init__(self, salary):
        self.salary = salary
        self.tax_min_breakpoints = {
            132407: 28,
            42708: 25,
            15528: 15,
            0: 0,
        }

    def get_rate(self):
        starting_from = list(self.tax_min_breakpoints.keys())

        for start in starting_from:
            if self.salary >= start:
                return self.tax_min_breakpoints[start]
                
        return None

    def calculate_tax(self):
        tax_rate = self.get_rate()
        total = self.salary * tax_rate / 100

        print('The tax for {} is {}%. That is {} dollars!'.format(self.salary, tax_rate, round(total)))


tax = Tax(gross)
tax.calculate_tax()
