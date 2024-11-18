import sys
input = sys.stdin.readline

def deploy(dist):
    s = L[0]
    times = 1

    for i in range(1,k):
        if L[i]-s > dist:
            s = L[i]
            times += 1

    return times >= m

def binsearch():
    lo = 0
    hi = int(1e9)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if deploy(mid):
            lo = mid
        else:
            hi = mid
    return hi

n,m,k = map(int,input().split())
L = list(map(int,input().split()))
d = binsearch()