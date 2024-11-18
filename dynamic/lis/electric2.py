import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
A.sort()
L = []
D = dict()
for i in A:
    L.append(i[1])
    D[i[1]] = i[0]

dp = [L[0]]
Ind = [0]

for a in L[1:]:
    if a > dp[-1]:
        dp.append(a)
        Ind.append(len(dp)-1)
    else:
        index = bisect_left(dp,a)
        dp[index] = a
        Ind.append(index)

print(n-len(dp))

Lis = set()
cur = len(dp)-1
for i in range(n-1,-1,-1):
    if Ind[i] == cur:
        cur -= 1
        Lis.add(L[i])

S = set(D.keys()) - Lis
Ans = []
for i in S:
    Ans.append(D[i])
Ans.sort()
for i in Ans:
    print(i)