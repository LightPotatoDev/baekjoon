n = int(input())
k = int(input())
MOD = int(1e9)+3
dp = [[0]*(n+1) for _ in range(k+1)]
for j in range(n):
    dp[0][j] = 1
    dp[1][j] = j


for i in range(2,k+1):
    for j in range(1,n+1):
        if j-2 < 0:
            continue
        dp[i][j] = (dp[i][j-1] + dp[i-1][j-2]) % MOD

print((dp[k-1][n-3] + dp[k][n-1]) % MOD)