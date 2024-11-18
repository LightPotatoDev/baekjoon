import sys
input = sys.stdin.readline

def divide(maxS):
    section = 1
    minN  = int(1e5)
    maxN  = 0

    for i in L:
        if max(maxN,i)-min(minN,i) <= maxS:
            minN = min(minN,i)
            maxN = max(maxN,i)
        else:
            section += 1
            minN = i
            maxN = i

    return section <= m


def binsearch():
    lo = -1
    hi = int(1e5)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if divide(mid):
            hi = mid
        else:
            lo = mid
    return hi

n,m = map(int,input().split())
L = list(map(int,input().split()))
print(binsearch())