while True:
    L = list(map(int,input().split()))

    if L[0] == 0:
        break

    L.sort()
    if L[0]**2 + L[1]**2 == L[2]**2:
        print("right")
    else:
        print("wrong")