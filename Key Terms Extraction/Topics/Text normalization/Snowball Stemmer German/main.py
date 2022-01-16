from nltk.stem import SnowballStemmer


# the following line reads a text from the input and converts it into a list
sent = input().split()

# write your code here
snowball = SnowballStemmer('german')
print('\n'.join(snowball.stem(word) for word in sent))
