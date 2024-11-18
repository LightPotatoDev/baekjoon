a,b,k = map(int,input().split())
if a>b:
    a,b = b,a

if k >= 0:
    if a == b:
        print("Second")
    else:
        print("First")
else:
    if a == b:
        if k == -1 or (a == 1 and b == 1):
            print("First")
        else:
            print("Second")
    else:
        if a == 0 and b == 1:
            print("Second")
        else:
            print("First")
