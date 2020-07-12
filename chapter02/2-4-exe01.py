# takes three numbers form user input then prints out the greatest number

# take input
x = input("Input the first number please: ")
y = input("Input the second number please: ")
z = input("Input the third number please: ")

x = float(x)
y = float(y)
z = float(z)

# test the numbers against each other and prints the greatest
# if (x >= y and x >= z):
#     print("{} is the greatest number".format(x))
# elif (y >= x and y>=z ):
#     print("{} is the greatest number".format(y))
# else:
#     print("{} is the greatest number".format(z))
#
max = x
if y > max:
    max = y
if z > max:
    max = z
print("{} is the greatest number".format(max))