# Iterative implementation of factorial

def factIt(n):
    """Assumes n an int > 0
       Returns n!"""
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

# Recursive implementation of factorial

def factRe(n):
    """Assumes n an int > 0
       Returns n!"""
    if n == 1:
        return 1
    else:
        return n*factRe(n - 1)

