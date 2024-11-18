import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
L = [[1]*m for _ in range(n)]
grid = [list(input().rstrip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
yi,xi,yf,xf = 0,0,0,0
dy = [-1,0,0,1]
dx = [0,-1,1,0]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            visited[i][j] = 1
            continue

        if grid[i][j] == 'S':
            yi,xi = i,j
            L[i][j] = 0
        if grid[i][j] == 'E':
            yf,xf = i,j

        for dir in range(4):
            ny,nx = i+dy[dir], j+dx[dir]
            if not ((0 <= ny < n) and (0 <= nx < m)):
                continue
            if grid[ny][nx] == '#':
                L[i][j] = 0

def grid_01bfs(yi,xi,yf,xf):
    dq = deque()
    dq.append([yi,xi])

    while dq:
        y,x = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if not ((0 <= ny < n) and (0 <= nx < m)):
                continue
            if visited[ny][nx] == 1:
                continue

            if L[ny][nx] == 0:
                dq.appendleft([ny,nx])
                L[ny][nx] = L[y][x]
            elif L[ny][nx] == 1:
                dq.append([ny,nx])
                L[ny][nx] = L[y][x] + 1
            visited[ny][nx] = 1

    return L[yf][xf]

print(grid_01bfs(yi,xi,yf,xf)+1)