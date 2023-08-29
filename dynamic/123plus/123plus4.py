import sys
input = sys.stdin.readline

dp = [[0,0,0],[1,0,0],[1,1,0],[2,0,1]] #starts with 1,2,3 (sorted)
mod = int(1e9)+9
for i in range(4,100001):
    a = sum(dp[i-1])%mod
    b = (dp[i-2][1] + dp[i-2][2])%mod
    c = dp[i-3][2]%mod
    dp.append([a,b,c])

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(dp[n])%mod)