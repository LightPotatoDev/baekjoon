import sys
input = sys.stdin.readline
import heapq

n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1
active = []
for i in range(n):
    for j in range(m):
        active.append((-L[i][j],i,j))
heapq.heapify(active)

dy = [0,-1,0,1]
dx = [1,0,-1,0]

while active:
    nn,y,x = heapq.heappop(active)
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if (0 <= ny < n) and (0 <= nx < m) and (L[ny][nx] > L[y][x]):
            dp[y][x] += dp[ny][nx]

print(dp[n-1][m-1])

for i in dp:
    print(i)