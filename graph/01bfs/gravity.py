import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
edge = [[[[1,1,0,0,0,0] for _ in range(m)] for _ in range(n)] for _ in range(2)]
yi,xi,yf,xf = -1,-1,-1,-1
dz = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dx = [0,0,0,0,1,-1]

GRAV_DOWN = 0
GRAV_UP = 1
FALL_DOWN = 2
FALL_UP = 3
MOVE_RIGHT = 4
MOVE_LEFT = 5

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'C':
            yi,xi = i,j
        elif grid[i][j] == 'D':
            yf,xf = i,j

def grounded(z,y,x):
    if z == GRAV_DOWN:
        return y+1 < n and grid[y+1][x] == '#'
    if z == GRAV_UP:
        return y-1 >= 0 and grid[y-1][x] == '#'

def moves(z,y,x):
    if z == GRAV_DOWN:
        if grounded(z,y,x):
            return [GRAV_UP,MOVE_LEFT,MOVE_RIGHT]
        else:
            return [FALL_DOWN]

    if z == GRAV_UP:
        if grounded(z,y,x):
            return [GRAV_DOWN,MOVE_LEFT,MOVE_RIGHT]
        else:
            return [FALL_UP]

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
            if grid[ny][nx] == '#':
                continue

            if cost[z][y][x] + edge[z][y][x][dir] < cost[nz][ny][nx]:
                cost[nz][ny][nx] = cost[z][y][x] + edge[z][y][x][dir]
                if edge[z][y][x][dir] == 0:
                    dq.appendleft([nz,ny,nx])
                elif edge[z][y][x][dir] == 1:
                    dq.append([nz,ny,nx])

    return min(cost[0][yf][xf], cost[1][yf][xf])

ans = grid_3d_01bfs(0,yi,xi,yf,xf)
if ans == int(1e7):
    ans = -1
print(ans)