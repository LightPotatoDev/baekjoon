import sys
input = sys.stdin.readline
from itertools import combinations

n,k = map(int,input().split())
L = [[i]+list(map(int,input().split())) for i in range(1,n+1)]

minF = int(1e15)
minC = []
comb = combinations(L,k)
for books in comb:
    S,M,m = 0,0,int(1e10)
    choice = []

    for b in books:
        choice.append(b[0])
        S += b[1]
        M = max(M,b[2])
        m = min(m,b[3])
    fatigue = S+M+m
    if fatigue < minF:
        minC = choice
        minF = fatigue

print(minF)
print(*minC)