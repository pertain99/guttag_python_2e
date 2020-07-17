def fib(n):
    """Assume n is integer
       return Fib of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('Fib of', i, fib(i))

testFib(6)