import sys
input = sys.stdin.readline

n,k = map(int,input().split())
L = [int(input()) for _ in range(n)]
SIZE = 65536+1

Tree = [0]*SIZE

def change(idx,add):
    while (idx <= SIZE):
        Tree[idx] += add
        idx += idx & -idx

def getSum(idx):
    s = 0
    while idx > 0:
        s += Tree[idx]
        idx &= (idx - 1)
    return s

def medianSearch():
    lo = 0
    hi = SIZE

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if getSum(mid) < (k+1)//2:
            lo = mid
        else:
            hi = mid
    return hi

ans = 0
for i in range(n):
    change(L[i]+1,1)
    if (i >= k):
        change(L[i-k]+1, -1)
    if (i >= k-1):
        ans += medianSearch()

print(ans-(n-k+1))
