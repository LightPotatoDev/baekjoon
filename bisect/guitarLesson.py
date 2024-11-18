n,m = map(int,input().split())
L = list(map(int,input().split()))

def blueray(size):
    s = 0
    times = 0
    i = 0

    while i < n:
        if times >= m:
            return False

        if s+L[i] < size:
            s += L[i]
            i += 1
        else:
            s = 0
            times += 1

    return True

def binsearch():
    lo = 0
    hi = int(1e4)*n

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if blueray(mid):
            hi = mid
        else:
            lo = mid
    return lo

print(binsearch())