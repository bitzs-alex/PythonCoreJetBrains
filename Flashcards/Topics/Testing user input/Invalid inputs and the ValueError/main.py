def check():
    try:
        num = int(input())
    except ValueError:
        print("Correct the error!")
    else:
        start, end = [25, 37]
        if start <= num <= end:
            print(num)
        else:
            print("Correct the error!")
