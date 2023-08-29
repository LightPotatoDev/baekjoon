import sys
input = sys.stdin.readline

dp = [[0,0,0],[1,0,0],[0,1,0],[1,1,1]] #ends with 1,2,3
mod = int(1e9)+9
for i in range(4,100001):
    a = (dp[i-3][0] + dp[i-3][1])%mod
    b = (dp[i-2][0] + dp[i-2][2])%mod
    c = (dp[i-1][1] + dp[i-1][2])%mod
    dp.append([c,b,a])

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(dp[n])%mod)