while True:
    a,b = map(int,input().split())
    if a == -1:
        break

    if a == 1 or b == 1:
        print(f"{a}+{b}={a+b}")
    else:
        print(f"{a}+{b}!={a+b}")