# enhanced version of square root calculator, can take in fraction number, negative number etc.
x = -1000
epsilon = 0.00001
numGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (low + high)/2.0
while abs(ans**3 - abs(x)) >= epsilon:
    numGuesses += 1
    if ans**3 < abs(x):
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
    print('low =', low, 'high =', high, 'abs(ans) =', ans, 'epsilon =', abs(ans**3 - abs(x)))
if x < 0:
    ans = -1 * ans
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

