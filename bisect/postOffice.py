import sys
input = sys.stdin.readline

n = int(input())
village = [tuple(map(int,input().split())) for _ in range(n)]

def dist(center):
    s = 0
    for pos,ppl in village:
        s += abs(pos-center) * ppl
    return s

lo = -int(1e9)
hi = int(1e9)
mid = 0

while lo+1 < hi:
    mid = (lo+hi)//2
    if dist(mid-1) <= dist(mid):
        hi = mid
    else:
        lo = mid

print(lo)