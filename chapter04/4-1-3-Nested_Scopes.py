def f(x):
    def g():
        x = 'abc'
        print('in g(): x =', x)
    def h():
        z = x
        print('in h(): z =', x)
    x = x + 1
    print('in f(): x =', x)
    h()
    g()
    print('in f(): x =', x)
    return g

x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()　　                                                 　　　　　　　　　　　　　　 　　