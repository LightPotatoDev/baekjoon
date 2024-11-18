import sys
input = sys.stdin.readline

def rest(dist):
    s = L[0]
    times = 0

    for i in range(1,n+2):
        while L[i]-s > dist:
            s += dist
            times += 1

            if times > m:
                return False
        s = L[i]

    return True

def binsearch():
    lo = 0
    hi = int(1e9)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if rest(mid):
            hi = mid
        else:
            lo = mid
    return hi

n,m,l = map(int,input().split())
L = list(map(int,input().split()))+[0,l]
L.sort()
print(binsearch())