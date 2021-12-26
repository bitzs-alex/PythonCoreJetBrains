# put your python code here
line_string = input().strip().lower().split(' ')

frequencies = {word: line_string.count(word) for word in line_string}

for frequency in frequencies.items():
    print(f'{frequency[0]} {frequency[1]}')
