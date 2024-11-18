import sys
input = sys.stdin.readline

n,m = map(int,input().split())
L = [int(input()) for _ in range(n)]
L.sort()

def entry(sec):
    entered = 0
    for i in L:
        entered += sec // i
        if entered >= m:
            return True

    return False

def binsearch():
    lo = 0
    hi = int(1e18)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if entry(mid):
            hi = mid
        else:
            lo = mid
    return hi

print(binsearch())