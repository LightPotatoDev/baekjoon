k,n = map(int,input().split())
DEPTH = 130

dp = [[0]*DEPTH for _ in range(n+1)]
dp[0][k] = 1

for i in range(n):
    for j in range(1,DEPTH - 1):
        dp[i+1][j-1] += dp[i][j]
        dp[i+1][j+1] += dp[i][j]

print(sum(dp[n][1:]))
