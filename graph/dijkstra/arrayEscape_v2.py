import sys
import heapq
input = sys.stdin.readline

n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j != 0:
            dp[i][j] = dp[i][j-1] + max(0,grid[i][j]-grid[i][j-1]+1)
        elif j == 0 and i != 0:
            dp[i][j] = dp[i-1][j] + max(0,grid[i][j]-grid[i-1][j]+1)
        elif i != 0 and j != 0:
            vCost = max(0,grid[i][j]-grid[i-1][j]+1)
            hCost = max(0,grid[i][j]-grid[i][j-1]+1)
            dp[i][j] = min(dp[i-1][j]+vCost,dp[i][j-1]+hCost)

print(dp[n-1][n-1])
