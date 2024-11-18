import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def grid_bfs(yi,xi):
    dq = deque([[yi,xi]])
    A[yi][xi] = areaID
    area = [[yi,xi]]

    while dq:
        y,x = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if not ((0 <= ny < n) and (0 <= nx < m)):
                continue

            if (L[ny][nx] == 1) and (A[ny][nx] == 0):
                A[ny][nx] = areaID
                area.append([ny,nx])
                dq.append([ny,nx])

    return len(area)


n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]

A = [[0]*m for _ in range(n)]
areaID = 1
areas = []
for i in range(n):
    for j in range(m):
        if (L[i][j] == 1) and (A[i][j] == 0):
            areas.append(grid_bfs(i,j))
            areaID += 1

print(len(areas))
print(max(areas, default=0))

