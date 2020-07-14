# enhanced version of square root calculator, can take in fraction number, negative number etc.

x = -0.25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (low + high)/2.0
while abs(ans**2 - abs(x)) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < abs(x):
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
print('numGuesses =', numGuesses)
if x < 0:
    print(str(ans) +'i' ' is close to square root of ' + str(x))
else:
    print(ans, 'is close to square root of', x)