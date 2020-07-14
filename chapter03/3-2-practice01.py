# input numbers
s = str(input("Enter comma separated numbers: "))

# convert to the list
l = s.split(",")
print(l)

# convert each element as float
li = []
for i in l:
    li.append(float(i))
print(li)

# compute sum
total = 0
total = sum(li)

print("Sum is: {}".format(total))