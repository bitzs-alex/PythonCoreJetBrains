starting_number = 1
final_number = 101
number_range = range(starting_number, final_number)

for number in number_range:
    is_5_multiple = (number % 5 == 0)
    is_3_multiple = (number % 3 == 0)

    if is_5_multiple and is_3_multiple:
        print('FizzBuzz')
    elif is_3_multiple:
        print('Fizz')
    elif is_5_multiple:
        print('Buzz')
    else:
        print(number)
