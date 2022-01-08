def object_with_beautiful_identity():
    final_val  = 10_000
    for i in range(final_val):
        # Change the next line
        if str(id(i)).endswith('888'):
            return i
    
    return -1
