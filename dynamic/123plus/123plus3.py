import sys
input = sys.stdin.readline

dp = [0,1,2,4]
mod = int(1e9)+9
for i in range(4,1000001):
    dp.append((dp[i-3]+dp[i-2]+dp[i-1])%mod)

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])