def find_my_list(all_lists, my_list):
    for index, lst in enumerate(all_lists):
        # Change the next line
        if lst is my_list:
            return index

print(list(map(lambda x : x*2, [1, 2, 3, 4])))
