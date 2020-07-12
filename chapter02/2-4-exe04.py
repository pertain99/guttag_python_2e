# takes 10 user input integers, then output the maximum odd number; if no odd number, output a message

i = 0
max_odd = None
while i < 10:
    x = int(input("Please enter an integer "))
    if x % 2 != 0:
        if max_odd is None:
            max_odd = x
        else:
            max_odd = max(max_odd, x)
    i += 1

if max_odd is not None:
    print(max_odd)
else:
    print("No odd number")

