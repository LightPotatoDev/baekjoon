import sys
input = sys.stdin.readline
from itertools import combinations

n,l,r,x = map(int,input().split())
A = list(map(int,input().split()))

cnt = 0
for i in range(2,len(A)+1):
    comb = combinations(A,i)
    for c in comb:
        c = list(c)
        c.sort()
        if c[-1]-c[0] >= x and l <= sum(c) <= r:
            cnt += 1
print(cnt)