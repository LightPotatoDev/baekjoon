n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
suffix = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if j == 0:
            suffix[i][j] = grid[i][j]
        else:
            suffix[i][j] = grid[i][j] + suffix[i][j-1]

dp = [[0]*m for _ in range(n)]

for j in range(m):
    dp[0][j] = suffix[0][j]

for i in range(1,n):
    sub_dp = [[0,0] for _ in range(m)]
    for j in range(m):
        if j == 0:
            sub_dp[j][0] = dp[i-1][j] + grid[i][j]
        else:
            sub_dp[j][0] = max(dp[i-1][j], sub_dp[j-1][0]) + grid[i][j]

    for j in range(m-1,-1,-1):
        if j == m-1:
            sub_dp[j][1] = dp[i-1][j] + grid[i][j]
        else:
            sub_dp[j][1] = max(dp[i-1][j], sub_dp[j+1][1]) + grid[i][j]
    for j in range(m):
        dp[i][j] = max(sub_dp[j])

print(dp[n-1][m-1])