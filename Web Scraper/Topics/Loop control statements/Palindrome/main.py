word = input()
new_word = ''

for char in word:
    new_word = char + new_word
    
print('Palindrome' if new_word == word else 'Not palindrome')
