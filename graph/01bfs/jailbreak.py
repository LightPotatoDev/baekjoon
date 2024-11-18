import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def grid_01bfs(yi,xi):
    dq = deque()
    dq.append([yi,xi])
    cost = [[int(1e7)]*m for _ in range(n)]
    cost[yi][xi] = 0

    while dq:
        y,x = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if not ((0 <= ny < n) and (0 <= nx < m)):
                continue
            if grid[ny][nx] == '*':
                continue

            nc = int(grid[ny][nx] == '#')
            if cost[ny][nx] > cost[y][x] + nc:
                cost[ny][nx] = cost[y][x] + nc
                if nc == 0:
                    dq.appendleft([ny,nx])
                elif nc == 1:
                    dq.append([ny,nx])

    return cost

T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    grid = [list(input().rstrip()) for _ in range(n)]
    yi1,xi1,yi2,xi2 = -1,-1,-1,-1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '$' and yi1 == -1:
                yi1,xi1 = i,j
            if grid[i][j] == '$' and yi1 != -1:
                yi2,xi2 = i,j

    for row in grid_01bfs(yi1,xi1):
        for j in range(m):
            if row[j] == int(1e7):
                row[j] = '#'
            row[j] = str(row[j])
        print(*row)
    print('')
    for row in grid_01bfs(yi2,xi2):
        for j in range(m):
            if row[j] == int(1e7):
                row[j] = '#'
            row[j] = str(row[j])
        print(*row)
    print('')
