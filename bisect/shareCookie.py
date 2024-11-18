import sys
input = sys.stdin.readline

def cookie(l):
    pieces = 0
    for i in L:
        pieces += i//l

    return pieces >= m

def binsearch():
    lo = 0
    hi = int(1e9)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if cookie(mid):
            lo = mid
        else:
            hi = mid
    return lo

m,n = map(int,input().split())
L = list(map(int,input().split()))
print(binsearch())