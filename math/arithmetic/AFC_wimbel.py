n,m = map(int,input().split())
a = n+m
b = n-m
if a%2 == 1 or b%2 == 1 or b<0:
    print(-1)
else:
    print(a//2,b//2)