from collections import Counter

user_input = input().lower()
print(sorted(Counter(user_input.split())))
