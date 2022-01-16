from collections import Counter
text = """all I want is a proper cup of coffee made in a proper copper coffee pot.
        I may be off my dot but I want a cup of coffee from a proper coffee pot."""
        
number = int(input().strip())
counter = sorted(Counter(text.split()).most_common(number), key=lambda word: word[1], reverse=True)

for count in counter:
    print(count[0], count[1])
