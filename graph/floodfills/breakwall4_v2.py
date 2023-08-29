import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
L = []
for _ in range(n):
    L.append(list(map(lambda x:(int(x)*-1),input().rstrip())))

dy = [-1,0,0,1]
dx = [0,-1,1,0]

areaID = 1
areas = []

def grid_bfs(start,areaID):
    dq = deque([start])
    L[start[0]][start[1]] = areaID
    size = 0
    while dq:
        y,x = dq.popleft()
        size += 1

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds and L[ny][nx] == 0:
                L[ny][nx] = areaID
                dq.append([ny,nx])

    areas.append(size)

def getAdj(y,x):
    S = set()
    for i in range(4):
        ny,nx = y+dy[i], x+dx[i]
        inbounds = (0 <= ny < n) and (0 <= nx < m)
        if inbounds and L[ny][nx] != -1:
            S.add(L[ny][nx])

    adj = 0
    for i in S:
        adj += areas[i-1]%10
    return (adj+1) % 10

for i in range(n):
    for j in range(m):
        if L[i][j] == 0:
            grid_bfs([i,j],areaID)
            areaID += 1

A = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if L[i][j] == -1:
            A[i][j] = getAdj(i,j)

for i in A:
    print(''.join(map(str,i)))