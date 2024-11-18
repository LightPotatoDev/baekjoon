import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dp[0][0] = 1
active = deque([(0,0)])

dy = [0,-1,0,1]
dx = [1,0,-1,0]

def nearPath(y,x):
    s = 0
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if (0 <= ny < n) and (0 <= nx < m) and (L[ny][nx] > L[y][x]):
            s += dp[ny][nx]

    return s

while active:
    y,x = active.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if (0 <= ny < n) and (0 <= nx < m) and (L[ny][nx] < L[y][x]):
            active.append((ny,nx))
            dp[ny][nx] = nearPath(ny,nx)

print(dp[n-1][m-1])
for i in dp:
    print(i)