import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    L = []
    D = defaultdict(int)
    for _ in range(4):
        L.append(list(map(int,input().split())))
    comb = combinations(L,2)
    for p1,p2 in comb:
        x1,y1 = p1
        x2,y2 = p2
        d = (x1-x2)**2 + (y1-y2)**2
        D[d] += 1

    Val = list(D.values())
    Val.sort()
    if Val[0] == 2 and Val[1] == 4:
        print(1)
    else:
        print(0)