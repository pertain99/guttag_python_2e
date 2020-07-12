# takes 10 user input integers, then output the maximum odd number; if not odd number, output a message

# takes 10 integers
iters = 0
while iters < 10:
    list[iters] = int(input("Please input the integer {} out of 10".format(iters)))
    iters += 1

# store the odd numbers into a new list
iters = 0
while iters < 10:
    n = list[iters]
    if (n % 2 != 0):
        list2[iters] = n

# find the maximum odd number
try:
    max_odd = max(list2)

# output a message if there is no odd number, otherwise, output the max_odd
if max_odd is None:
    print("No odd number among the 10 numbers")
else:
    print("{} is the maximum odd number".format{max_odd})

