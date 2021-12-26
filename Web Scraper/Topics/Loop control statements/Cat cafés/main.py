max_cafe = ''
break_point = 'MEOW'
cafe_dictionary = {}

while True:
    cafe = input().strip()
    
    if cafe == break_point:
        break
    
    cafe = cafe.split(' ')
    cafe_dictionary[int(cafe[1])] = cafe[0]
    
maximum = max(cafe_dictionary.keys())
print(cafe_dictionary[maximum])
