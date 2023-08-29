import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
L = []
for i in range(n):
    line = list(map(int,input().rstrip().split()))
    L.append(line)

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def grid_bfs(grid):
    dq = deque()
    dq.append([0,0])
    grid[0][0] = 6
    allmelt = True

    while dq:
        y,x = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds:
                if grid[ny][nx] == 0:
                    dq.append([ny,nx])
                    grid[ny][nx] = 6
                elif grid[ny][nx] <= 5:
                    grid[ny][nx] += 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] >= 3:
                if 3 <= grid[i][j] <= 5:
                    allmelt = False
                grid[i][j] = 0
            elif grid[i][j] != 0:
                grid[i][j] = 1

    return (grid, allmelt)

cnt = 0
while True:
    L, flag = grid_bfs(L)
    if flag == True:
        break
    cnt += 1
print(cnt)