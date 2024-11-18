import sys
input = sys.stdin.readline

n,m = map(int,input().split())
L = [int(input()) for _ in range(n)]

def spend(k):
    fajo = 1
    money = 0
    for i in L:
        if k < i:
            return False #k+

        if money+i <= k:
            money += i
        else:
            money = i
            fajo += 1


    if fajo <= m:
        return True #k-
    else:
        return False #k+

def binsearch():
    lo = 0
    hi = int(1e10)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if spend(mid):
            hi = mid
        else:
            lo = mid
    return hi

print(binsearch())