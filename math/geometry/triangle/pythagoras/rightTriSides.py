i = 0
while True:
    i += 1
    a,b,c = map(int,input().split())
    if a == 0:
        break

    print(f"Triangle #{i}")
    if a == -1:
        a = (c**2-b**2)**0.5
        if c**2-b**2 > 0:
            print("a = " + "{:.3f}".format(a))
        else:
            print("Impossible.")
    elif b == -1:
        b = (c**2-a**2)**0.5
        if c**2-a**2 > 0:
            print("b = " + "{:.3f}".format(b))
        else:
            print("Impossible.")
    else:
        c = (a**2 + b**2) ** 0.5
        print("c = " + "{:.3f}".format(c))
    print('')