import sys
input = sys.stdin.readline
from bisect import bisect_right
from collections import defaultdict

n,k = map(int,input().split())
Jewel = [list(map(int,input().split())) for _ in range(n)]
Bag = [int(input()) for _ in range(k)]
BagDict = defaultdict(int)

Jewel.sort(key=lambda x:(-x[1],x[0]))
Bag.sort()
for i in Bag:
    BagDict[i] += 1
val = 0
for m,v in Jewel:
    ind = bisect_right(Bag,m)-1
    cap = Bag[ind]
    if cap < m:
        continue
    while BagDict[cap] == 0:
        ind += 1
        cap = Bag[ind]

    BagDict[cap] -= 1
    val += v

print(val)
