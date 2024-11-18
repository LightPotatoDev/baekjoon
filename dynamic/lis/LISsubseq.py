import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    L = [int(input()) for _ in range(n)]

    def lis(L):
        dp = [L[0]]
        s = 1

        for a in L[1:]:
            if a > dp[-1]:
                dp.append(a)
            else:
                index = bisect_left(dp,a)
                dp[index] = a
            s += len(dp)

        return s

    sum = 0
    for i in range(n):
        sum += lis(L[i:])

    print(f"Case #{tc+1}: {sum}")