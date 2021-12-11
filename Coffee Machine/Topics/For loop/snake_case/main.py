word = input()
final_word = ''
underscore = '_'

for char in word:
    if char.isupper():
        final_word += underscore
        char = char.lower()

    final_word += char

print(final_word)
