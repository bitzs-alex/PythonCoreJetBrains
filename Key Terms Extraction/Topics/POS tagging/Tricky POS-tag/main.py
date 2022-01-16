import nltk

nltk.data.path.append(r'C:\\Users\\mblon\\OneDrive - 충남대학교\\PythonLearning\\nltk_data')

sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']
print(nltk.pos_tag(sent)[sent.index('raced')][1])
