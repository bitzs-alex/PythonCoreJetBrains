# put your python code here
square_sum = 0
total_sum = 0

while True:
    number = int(input().strip())
    total_sum += number
    square_sum += (number ** 2)

    if total_sum == 0:
        break

print(square_sum)
