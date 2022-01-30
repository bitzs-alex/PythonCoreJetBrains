import re

class WordError(Exception):
    def __str__(self):
        return "This is the word contains W error"


def check_w_letter(word):
    match = re.search('w', word)
    if match:
        raise WordError

    return word
