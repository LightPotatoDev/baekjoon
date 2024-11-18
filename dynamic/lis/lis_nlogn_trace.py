import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
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

print(len(dp))

Ans = []
cur = len(dp)-1
for i in range(n-1,-1,-1):
    if Ind[i] == cur:
        cur -= 1
        Ans.append(L[i])

print(*Ans[::-1])