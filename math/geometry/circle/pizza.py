i = 0
while True:
    i += 1
    L = list(map(int,input().split()))
    if L[0] == 0:
        break
    r,w,l = L

    rad = 4*r**2
    diag = w**2 + l**2
    if rad >= diag:
        print(f"Pizza {i} fits on the table.")
    else:
        print(f"Pizza {i} does not fit on the table.")