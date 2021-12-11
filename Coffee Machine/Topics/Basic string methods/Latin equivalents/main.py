name = input()

def normalize(converted_name):

    # put your code here
    normalized_chars = {
        'é': 'e',
        'ë': 'e',
        'á': 'a',
        'å': 'a',
        'œ': 'oe',
        'æ': 'ae',
    }
    new_name = converted_name
    latin_keys = normalized_chars.keys()
    
    for latin in latin_keys:
        new_name = new_name.replace(latin, normalized_chars[latin])

    return new_name

print(normalize(name))
