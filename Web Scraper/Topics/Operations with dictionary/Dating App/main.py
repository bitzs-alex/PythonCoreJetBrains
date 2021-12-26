def select_dates(potential_dates):
    berlin = 'Berlin'
    age = 30
    art = 'art'
    
    return ', '.join([
        date['name'] for date in potential_dates 
        if date['age'] > age and art in date['hobbies'] and date['city'] == berlin
    ])
