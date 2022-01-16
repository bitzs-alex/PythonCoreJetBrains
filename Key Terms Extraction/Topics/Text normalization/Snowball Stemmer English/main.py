from nltk.stem import SnowballStemmer


# the following line reads a text from the input and converts it into a list
sent = input().split()
stemmer = SnowballStemmer('english')

# write your code here
print('\n'.join(stemmer.stem(word) for word in sent))
