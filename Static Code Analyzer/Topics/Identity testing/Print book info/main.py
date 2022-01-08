def print_book_info(title, author=None, year=None):
    info = f'"{title}"'
    
    if author is not None and year is not None:
        info = f'"{title}" was written by {author} in {year}'
    elif year is not None:
        info = f'"{title}" was written in {year}'
    elif author is not None:
        info = f'"{title}" was written by {author}'
        
    print(info)
