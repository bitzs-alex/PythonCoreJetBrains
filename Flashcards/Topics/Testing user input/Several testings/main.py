def check(number):
    try:
        number = int(number)
    except ValueError:
        print('It is not a number!')
    else:
        least = 201
        if number >= least:
            print(number)
        else:
            print("There are less than 202 apples! You cheated me!")
