def translate(**kwargs):
    for word_1, word_2 in words.items():
        print(word_1, ":", word_2)

words = {"mother": "madre", "father": "padre", 
         "grandmother": "abuela", "grandfather": "abuelo"}

translate(**words)
