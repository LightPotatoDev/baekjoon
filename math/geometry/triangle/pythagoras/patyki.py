L = list(map(int,input().split()))
L.sort()
a,b,c = L

if a**2 + b**2 == c**2:
    print(1)
elif a == b and b == c:
    print(2)
else:
    print(0)
