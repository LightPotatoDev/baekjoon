import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
L = []
Check = [[-1]*m for _ in range(n)]
for _ in range(n):
    L.append(list(map(int,input().split())))

dy = [0,-1,0,1]
dx = [-1,0,1,0]

areaID = 0
aSize = []

def grid_bfs(start,areaID):
    dq = deque([start])
    Check[start[0]][start[1]] = areaID
    size = 0
    while dq:
        y,x = dq.popleft()
        size += 1

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            blocked = ((L[y][x] >> i) & 1) == 1
            if (not blocked) and inbounds and Check[ny][nx] == -1:
                Check[ny][nx] = areaID
                dq.append([ny,nx])

    aSize.append(size)

def merge(y,x):
    s = 0
    for i in range(4):
        ny,nx = y+dy[i], x+dx[i]
        inbounds = (0 <= ny < n) and (0 <= nx < m)
        if inbounds and Check[ny][nx] != Check[y][x]:
            mySize = aSize[Check[y][x]]
            othSize = aSize[Check[ny][nx]]
            s = max(s, mySize+othSize)
    return s

for i in range(n):
    for j in range(m):
        if Check[i][j] == -1:
            grid_bfs([i,j],areaID)
            areaID += 1

print(len(aSize))
print(max(aSize))

maxSize = 0
for i in range(n):
    for j in range(m):
        maxSize = max(merge(i,j),maxSize)
print(maxSize)