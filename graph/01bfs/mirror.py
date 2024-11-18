import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = n
grid = [list(input().rstrip()) for _ in range(n)]
edge = [[[[1,1,0,0,0,0] for _ in range(m)] for _ in range(n)] for _ in range(2)]
yi,xi,yf,xf = -1,-1,-1,-1
dz = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dx = [0,0,0,0,1,-1]

VERTICAL = 0
HORIZONTAL = 1
DOWN = 2
UP = 3
RIGHT = 4
LEFT = 5

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            if yi == -1:
                yi,xi = i,j
            else:
                yf,xf = i,j

def moves(z,y,x):
    if z == VERTICAL:
        if grid[y][x] == '!':
            return [HORIZONTAL,DOWN,UP]
        else:
            return [DOWN,UP]

    if z == HORIZONTAL:
        if grid[y][x] == '!':
            return [VERTICAL,RIGHT,LEFT]
        else:
            return [RIGHT,LEFT]

def grid_3d_01bfs(zi,yi,xi,yf,xf):
    dq = deque()
    dq.append([zi,yi,xi])
    cost = [[[int(1e7)]*m for _ in range(n)] for _ in range(2)]
    cost[zi][yi][xi] = 0

    while dq:
        z,y,x = dq.popleft()

        for dir in moves(z,y,x):
            nz,ny,nx = z+dz[dir], y+dy[dir], x+dx[dir]
            if not ((0 <= nz < 2) and (0 <= ny < n) and (0 <= nx < m)):
                continue
            if grid[ny][nx] == '*':
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
    ans = min(ans,grid_3d_01bfs(i,yi,xi,yf,xf))
print(ans)