import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
graph = [[] for _ in range(n)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            isWall[i][j] = 1
            continue

        if grid[i][j] == 'S':
            yi,xi = i,j
        if grid[i][j] == 'E':
            yf,xf = i,j

        for dir in range(4):
            ny,nx = i+dy[dir], j+dx[dir]
            if not ((0 <= ny < n) and (0 <= nx < m)):
                continue
            if grid[ny][nx] == '#':
                nearWall[i][j] = 1

for i in range(n):
    for j in range(m):
        for dir in range(4):
            ny,nx = i+dy[dir], j+dx[dir]
            if not ((0 <= ny < n) and (0 <= nx < m)):
                continue
            if nearWall[i][j] == 1 and nearWall[ny][nx] == 1:
                edge[i][j][dir] = 0


def grid_01bfs(yi,xi,yf,xf):
    dq = deque()
    dq.append([yi,xi])
    cost = [[int(1e7)]*m for _ in range(n)]
    cost[yi][xi] = 0

    while dq:
        y,x = dq.popleft()

        for dir in range(4):
            ny,nx = y+dy[dir], x+dx[dir]
            if not ((0 <= ny < n) and (0 <= nx < m)):
                continue
            if isWall[ny][nx]:
                continue

            if cost[y][x] + edge[y][x][dir] < cost[ny][nx]:
                cost[ny][nx] = cost[y][x] + edge[y][x][dir]
                if edge[y][x][dir] == 0:
                    dq.appendleft([ny,nx])
                elif edge[y][x][dir] == 1:
                    dq.append([ny,nx])

    return cost[yf][xf]

print(grid_01bfs(yi,xi,yf,xf))