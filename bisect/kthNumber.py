import sys
input = sys.stdin.readline

def finding(m):
    smaller = 0
    for i in range(1,n+1):
        smaller += min(n,m//i)
    return smaller < k

def binsearch():
    lo = 0
    hi = int(1e9)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if finding(mid):
            lo = mid
        else:
            hi = mid
    return hi

n = int(input())
k = int(input())
print(binsearch())