t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print('t1:', t1)
print('t2:', t2)
print('t1 + t2:', t1 + t2)
print('(t1 + t2)[3]:', (t1 + t2)[3])
print('(t1 + t2)[2:5]:', (t1 + t2)[2:5])

def intersect(t1, t2):
    """Assume t1 and t2 are tuples
       Returns a tuple containing elements that are in both t1 and t2"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

#t1 = (1, 2, 3)
#t2 = (3, 4, 5, 1)

print(intersect(t1, t2))