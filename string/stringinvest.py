while True:
    try:
        L = [0,0,0,0]
        s = input()
        for i in s:
            if i.islower():
                L[0] += 1
            elif i.isupper():
                L[1] += 1
            elif i.isnumeric():
                L[2] += 1
            else:
                L[3] += 1
        print(*L)
    except EOFError:
        break
