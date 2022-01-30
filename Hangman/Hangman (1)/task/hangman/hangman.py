#
# Write your code here
# import random
#
# print('H A N G M A N')
# word_bank = ['python', 'java', 'kotlin', 'javascript']
# hidden = random.choice(word_bank)
# hyphened = ['-' for _ in range(len(hidden))]
# trials = 8
#
# while trials > 0:
#     print()
#     print(''.join(hyphened))
#     letter = input(f"Input a letter: ")
#     trials -= 1
#
#     if letter in hidden:
#         word = hidden
#
#         for index, char in enumerate(word):
#             if char == letter:
#                 hyphened[index] = letter
#
#         continue
#
#     print("That letter doesn't appear in the word")
#
# # if hidden == hyphened:
# #     print("You survived!")
# # else:
# print("Thanks for playing!"
#       + "\nWe'll see how well you did in the next stage")
