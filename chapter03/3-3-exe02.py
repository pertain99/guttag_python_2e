# enhanced version of square root calculator, can take in fraction number, negative number etc.

x = -0.001
epsilon = 0.001
numGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (low + high)/2.0
while abs(ans**3 - abs(x)) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans, 'abs(ans**3 - abs(x))', abs(ans**3 - abs(x)))
    numGuesses += 1
    if ans**3 < abs(x):
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
if x < 0:
    ans = -1 * ans
    print('low =', low, 'high =', high, 'ans =', ans, 'abs(ans**3 - abs(x))', abs(ans**3 - abs(x)))
    print('numGuesses =', numGuesses + 1)
    print(ans, 'is close to square root of', x)
else:
    print('low =', low, 'high =', high, 'ans =', ans, 'abs(ans**3 - abs(x))', abs(ans**3 - abs(x)))
    print('numGuesses =', numGuesses + 1)
    print(ans, 'is close to square root of', x)