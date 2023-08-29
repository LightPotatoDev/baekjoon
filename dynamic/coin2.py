k,n = map(int,input().split())
coins = [0]+[int(input()) for _ in range(n)]
dp = [[int(1e5)]*(k+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 0

for i in range(1,n+1):
    val = coins[i]

    for j in range(1,k+1):
        if val > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-val]+1)

if dp[n][k] == int(1e5):
    print(-1)
else:
    print(dp[n][k])
for row in dp:
    print(row)