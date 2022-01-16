from nltk.stem import WordNetLemmatizer


# your code here
lemma = WordNetLemmatizer()
word = input().strip()
print(
    lemma.lemmatize(word),
    lemma.lemmatize(word, 'a'),
    lemma.lemmatize(word, 'v'),
    sep='\n',
)
