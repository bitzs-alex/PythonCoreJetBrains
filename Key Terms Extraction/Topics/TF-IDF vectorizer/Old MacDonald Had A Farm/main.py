#  write your code here 
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(input='file', use_idf=True, lowercase=True,
                             analyzer='word', ngram_range=(1, 1),
                             stop_words=None)
with open('dataset.txt', 'r') as file:
    tfidf_matrix = vectorizer.fit_transform([file])

print(tfidf_matrix)
