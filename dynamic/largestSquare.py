n,m = map(int,input().split())
grid = [list(map(int,input())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for j in range(m):
    dp[0][j] = grid[0][j]

for i in range(n):
    dp[i][0] = grid[i][0]

for i in range(1,n):
    for j in range(1,m):
        if grid[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(max([max(r) for r in dp]) ** 2)