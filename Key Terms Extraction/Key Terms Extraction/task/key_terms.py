import re
from collections import Counter
import nltk
import string

from lxml import etree
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer


# To bypass the Lookup error for the dataset
nltk.data.path.append('C:\\Users\\mblon\\OneDrive - 충남대학교\\PythonLearning\\nltk_data')

corpus = etree.parse("news.xml").getroot()[0]
punctuations = stopwords.words('english') + list(string.punctuation) + ['ha', 'wa', 'u', 'a']
headings = []
dataset = []

for news in corpus:
    headings.append(news[0].text + ':')
    tokens = word_tokenize(news[1].text.lower())
    normalizer = WordNetLemmatizer()
    normalized = [
        normalizer.lemmatize(word)
        for word in tokens
    ]
    # nltk_data/corpora/wordnet/noun.exc
    normalized = [
        word
        for word in normalized
        if word not in punctuations
        and nltk.pos_tag([word])[0][1] == 'NN'
    ]
    dataset.append(' '.join(normalized))

vectorizer = TfidfVectorizer()
weighted_matrix = vectorizer.fit(dataset)
terms = vectorizer.get_feature_names_out()

for key, sentence in enumerate(dataset):
    print(headings[key])
    indexed = enumerate(vectorizer.transform([sentence]).toarray()[0])
    frequent_5 = sorted(indexed, key=lambda t: t[1], reverse=True)[:10]
    word_freq = sorted([(terms[index], value) for index, value in frequent_5], reverse=True)

    print(' '.join([
        word
        for word, freq in sorted(word_freq, key=lambda t: t[1], reverse=True)[:5]
    ]))

    if sentence is not dataset[-1]:
        print()
