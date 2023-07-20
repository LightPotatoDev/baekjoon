import sys
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
dp = [L[0]]
dp2 = deque([[L[0]]])
longestI = 0
prevLongest = 0

for i,a in enumerate(L[1:]):
    if a > dp[-1]:
        dp.append(a)
        if i+1-longestI > 0:
            for j in range(longestI-prevLongest):
                dp2.popleft()
            prevLongest = longestI
        longestI = i
    else:
        index = bisect_left(dp,a)
        dp[index] = a
    dp2.append(dp[:])
    print(dp2,i, longestI, prevLongest)

print(len(dp))

for i in range(len(dp)):
    print(dp2[longestI+i][i], end=' ')
