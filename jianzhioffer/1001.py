while True:
    try:
        print("Input two integers, separated by space, e.g. ' 1 2'")
        line = input()
        a = line.split()
        print(int(a[0]) + int(a[1]))
    except:
        break
