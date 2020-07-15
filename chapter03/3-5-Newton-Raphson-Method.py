# Using Newton-Raphson method to find square root
# Find x, such that x**2 - 24 is between epsilon and 0

epsilon = 0.01
k = 24.0

guess = k/2.0
numGuesses = 0
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    numGuesses += 1
print('Newton-Raphson Method:')
print('Square root of', k, 'is about', guess)
print('Number of guesses is', numGuesses)

# Bisection Search Method:
low = min(0.0, k)
high = max(1.0, k)
guess = (low + high)/2.0
numGuesses = 0
while abs(guess**2 - k) >= epsilon:
    if guess**2 < k:
        low = guess
    else:
        high = guess
    guess = (low + high)/2.0
    numGuesses += 1
print('Bisection Search Method:')
print('Square root of', k, 'is about', guess)
print('Number of guesses is', numGuesses)
