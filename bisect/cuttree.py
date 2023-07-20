import sys
input = sys.stdin.readline

n,m = map(int,input().split())
L = list(map(int,input().split()))

lo = 0
hi = max(L)

while lo + 1 < hi:
    mid = (lo + hi) // 2
    s = sum([i-mid for i in L if i-mid>0])
    if s >= m:
        lo = mid
    else:
        hi = mid

print(lo)