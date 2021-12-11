# put your python code here
start = int(input())
end = int(input()) + 1
multiples = []

for number in range(start, end):
    if number % 3 == 0:
        multiples.append(number)

print(sum(multiples) / len(multiples))
