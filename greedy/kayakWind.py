n,s,r = map(int,input().split())
L = [1]*(n)
broken = list(map(int,input().split()))
extra  = list(map(int,input().split()))

for i in broken:
    L[i-1] -= 1

for i in extra:
    L[i-1] += 1

for i in range(n):
    if L[i] == 2:
        if i-1 >= 0 and L[i-1] == 0:
            L[i-1] += 1
            L[i] -= 1
        elif i+1 < n and L[i+1] == 0:
            L[i+1] += 1
            L[i] -= 1

print(L.count(0))