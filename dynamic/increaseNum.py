n = int(input())
dp = [[1]*10 for _ in range(n)]
mod = 10007

for i in range(1,n):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j]+dp[i][j-1])%mod

print(sum(dp[n-1])%mod)