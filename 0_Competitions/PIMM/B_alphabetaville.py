n,m = map(int,input().split())
L = list(map(int,input().split()))
Friends = set(map(int,input().split()))

ok = 0
for i in range(m):
    if L[i] in Friends:
        ok += 1
print(m - ok)