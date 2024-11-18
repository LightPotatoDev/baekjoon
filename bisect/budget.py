n = int(input())
L = list(map(int,input().split()))
L.sort()
m = int(input())

lo = 0
hi = L[-1]
s = 0

def budget(lim):
    s = 0
    for i in L:
        if i < lim:
            s += i
        else:
            s += lim
    return s

while lo + 1 < hi:
    mid = (lo + hi) // 2
    s = budget(mid)

    if s < m:
        lo = mid
    else:
        hi = mid

if budget(hi) <= m:
    print(hi)
else:
    print(lo)