multiples = []
counter = int(input())

for _ in range(counter):
    number = int(input().strip())

    if number % 7 == 0:
        multiples.append(number ** 2)

for multiple in multiples:
    print(multiple)
