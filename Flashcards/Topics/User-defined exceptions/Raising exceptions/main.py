class NegativeSumError(Exception):
    def __str__(self):
        return "this is from str function"
        
        
def sum_with_exceptions(a, b):
    total = a + b
    if total < 0:
        raise NegativeSumError

    return total
