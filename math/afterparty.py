l,p = map(int,input().split())
L = list(map(int,input().split()))
print(*[i-l*p for i in L])