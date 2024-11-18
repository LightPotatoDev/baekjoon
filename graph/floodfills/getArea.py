import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
L = [[0]*m for _ in range(n)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            L[i][j] = -1

dy = [-1,0,0,1]
dx = [0,-1,1,0]

areaID = 1
areas = []

def grid_bfs(start,areaID):
    dq = deque([start])
    yi,xi = start
    mode = L[yi][xi]
    L[yi][xi] = areaID
    size = 0
    while dq:
        y,x = dq.popleft()
        size += 1

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds and L[ny][nx] == mode:
                L[ny][nx] = areaID
                dq.append([ny,nx])

    areas.append(size)

for i in range(n):
    for j in range(m):
        if L[i][j] == 0:
            grid_bfs([i,j],areaID)
            areaID += 1
print(areaID-1)
areas.sort()
print(*areas)