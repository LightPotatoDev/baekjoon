n,m = map(int,input().split())

if n==1:
    print(1)
elif n==2:
    if m >= 7:
        print(4)
    else:
        print((m+1)//2)
    # min((m+1)//2, 4)
else:
    if m <= 4:
        print(m)
    elif 5 <= m <= 6:
        print(4)
    # min(m, 4)
    else:
        print(m-2)