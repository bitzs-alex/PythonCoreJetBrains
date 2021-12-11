string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
counter = 0

for char in string:
    if char in vowels:
        counter += 1

print(counter)
