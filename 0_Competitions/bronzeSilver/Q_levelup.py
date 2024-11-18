import sys
input = sys.stdin.readline

T = int(input())

def level(lv,exp):
    reqExp = lv*(lv+1)
    if reqExp <= exp:
        return True
    else:
        return False

def binsearch(exp):
    lo = 0
    hi = int(1e9)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if level(mid,exp):
            lo = mid
        else:
            hi = mid
    return hi

for _ in range(T):
    n = int(input())
    exp = (n * (n+1)) // 2
    print(binsearch(exp))

