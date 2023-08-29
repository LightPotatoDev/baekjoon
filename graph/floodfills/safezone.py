import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int,input().rstrip().split())))

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def grid_bfs(L):

    def fill(r,c):
        dq = deque([(r,c)])

        while dq:
            y,x = dq.popleft()
            L[y][x] = 1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                inbounds = 0 <= ny < n and 0 <= nx < n
                if inbounds and L[ny][nx] == 0:
                    dq.append((ny,nx))
                    L[ny][nx] = 1

    area = 0
    for i in range(n):
        for j in range(n):
            if L[i][j] == 0:
                area += 1
                fill(i,j)

    return area

def print2d(L):
    for row in L:
        print(row)

def safezone(height):
    L = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            L[i][j] = int(grid[i][j] <= height)
    return L

maxZone = 0
for i in range(100):
    A = safezone(i)
    maxZone = max(maxZone,grid_bfs(A))

print(maxZone)
