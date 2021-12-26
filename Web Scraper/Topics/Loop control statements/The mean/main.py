numbers = []
break_point = '.'

while True:
    number = input()

    if number == break_point:
        break

    numbers.append(int(number))

print(sum(numbers) / len(numbers))
