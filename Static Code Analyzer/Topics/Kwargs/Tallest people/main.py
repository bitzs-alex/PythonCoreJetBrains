def tallest_people(**peoples):
    tallest = max(peoples.values())
    tallest_list = list(filter(lambda person: person[1] == tallest, peoples.items()))
    print('\n'.join([f"{person[0]} : {person[1]}" for person in sorted(tallest_list)]))
