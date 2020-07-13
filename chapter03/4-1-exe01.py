# chapter 03: exhuastive enumeration
# takes user input one integer, then output root and pwr, if not exist integer solution, output a message

x = int(input("Please enter an integer: "))

root = 0
pwr = 0

if x < 0:
    print('{} is a negative number, no real solution'.format(x))
else:
    while root**2 < abs(x):
        root = root + 1
    print('{} is root'.format(root))

pwr = x**2

print('{} is power'.format(pwr))

