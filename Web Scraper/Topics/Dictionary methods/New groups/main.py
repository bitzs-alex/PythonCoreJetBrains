# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
group_num = int(input().strip())
groups_dictionary = {}

for i in range(group_num):
    groups_dictionary[groups[i]] = int(input().strip())
    
groups_dictionary.update(dict.fromkeys(groups[group_num:], None))
print(groups_dictionary)
