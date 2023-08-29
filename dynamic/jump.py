n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue

        ny = i+board[i][j]
        nx = j+board[i][j]

        if 0<=ny<n:
            dp[ny][j] += dp[i][j]
        if 0<=nx<n:
            dp[i][nx] += dp[i][j]

print(dp[n-1][n-1])

