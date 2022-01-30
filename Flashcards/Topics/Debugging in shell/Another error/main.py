def add_underscores(word):
    new_word = '_'
    for i in word:
        new_word += i + '_'
    return new_word


print(add_underscores(input()))
