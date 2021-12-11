string = input()
punctuation_list = ',.!?'

for punctuation in punctuation_list:
    string = string.replace(punctuation, '')
    
print(string.lower())
