import re

password = input()
# your code here
match = re.search(r"^\w{6,15}$", password, flags=re.ASCII)
print('Thank you!' if match else 'Error!')
