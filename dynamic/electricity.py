import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int,input().split())))
lines.sort()
L = [i[1] for i in lines]
dp = [L[0]]

for a in L[1:]:
    if a > dp[-1]:
        dp.append(a)
    else:
        index = bisect_left(dp,a)
        dp[index] = a

print(n-len(dp))