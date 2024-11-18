import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]

def lis(L):
    dp = [L[0]]

    for a in L[1:]:
        if a > dp[-1]:
            dp.append(a)
        else:
            index = bisect_left(dp,a)
            dp[index] = a

    return len(dp)

print(n-lis(L))