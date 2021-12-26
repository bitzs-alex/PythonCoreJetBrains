# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
values = list(test_dict.values())
keys = list(test_dict.keys())
min_index = values.index(min(values))
max_index = values.index(max(values))

print(f'min: {keys[min_index]}')
print(f'max: {keys[max_index]}')
