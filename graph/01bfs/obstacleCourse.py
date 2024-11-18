import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = n
grid = [list(input().rstrip()) for _ in range(n)]
edge = [[[[0,0,1,0,0,1] for _ in range(m)] for _ in range(n)] for _ in range(2)]
yi,xi,yf,xf = 0,0,0,0
dy = [1,-1,0,0,0,0]
dx = [0,0,0,1,-1,0]
dz = [0,0,1,0,0,-1]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'A':
            yi,xi = i,j
        if grid[i][j] == 'B':
            yf,xf = i,j


def grid_3d_01bfs(zi,yi,xi,zf,yf,xf):
    dq = deque()
    dq.append([zi,yi,xi])
    cost = [[[int(1e7)]*m for _ in range(n)] for _ in range(2)]
    cost[zi][yi][xi] = 0

    while dq:
        z,y,x = dq.popleft()

        for dir in range(6):
            nz,ny,nx = z+dz[dir], y+dy[dir], x+dx[dir]
            if not ((0 <= nz < 2) and (0 <= ny < n) and (0 <= nx < m)):
                continue
            if 0 <= dir <= 1 and z == 1:
                continue
            if 3 <= dir <= 4 and z == 0:
                continue
            if grid[ny][nx] == 'x':
                continue

            if cost[z][y][x] + edge[z][y][x][dir] < cost[nz][ny][nx]:
                cost[nz][ny][nx] = cost[z][y][x] + edge[z][y][x][dir]
                if edge[z][y][x][dir] == 0:
                    dq.appendleft([nz,ny,nx])
                elif edge[z][y][x][dir] == 1:
                    dq.append([nz,ny,nx])

    return min(cost[0][yf][xf], cost[1][yf][xf])

ans = int(1e7)
for i in range(2):
    ans = min(ans,grid_3d_01bfs(i,yi,xi,0,yf,xf))
print(ans)