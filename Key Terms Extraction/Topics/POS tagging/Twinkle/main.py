import nltk

# specifying dataset path (i.e. I downloaded the dataset at different location)
nltk.data.path.append(r'C:\\Users\\mblon\\OneDrive - 충남대학교\\PythonLearning\\nltk_data')

poem = ['Twinkle', ',', 'twinkle', ',', 'little', 'star', ',',
        'How', 'I', 'wonder', 'what', 'you', 'are', '.',
        'Up', 'above', 'the', 'world', 'so', 'high', ',',
        'Like', 'a', 'diamond', 'in', 'the', 'sky', '.']
tagged = nltk.pos_tag(poem)
print('\n'.join(word for word, tag in tagged if tag == 'NN'))
