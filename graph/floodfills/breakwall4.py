import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
L = []
for _ in range(n):
    row = list(map(lambda x:(int(x)*-1),input().rstrip()))
    L.append(row)

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def grid_bfs(start,areaID):
    dq = deque()
    dq.append(start)
    adj = [start]
    while dq:
        y,x = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds and L[ny][nx] == 0:
                dq.append([ny,nx])
                adj.append([ny,nx])

        for y,x in adj:
            L[y][x] = (len(adj),areaID)

def getAdj(y,x):
    S = set()
    for i in range(4):
        ny,nx = y+dy[i], x+dx[i]
        inbounds = (0 <= ny < n) and (0 <= nx < m)
        if inbounds and L[ny][nx] != -1:
            S.add(L[ny][nx])

    adj = 0
    for i in S:
        adj += i[0]
    return (adj+1) % 10

areaID = 0
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