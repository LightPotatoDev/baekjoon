import sys
import copy
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
L = []
for _ in range(n):
    L.append(list(map(int,input().rstrip())))

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def grid_bfs(start,first):
    dq = deque()
    dq.append(start)
    touchWalls = []
    A = copy.deepcopy(L)
    A[0][0] = 2
    while dq:
        y,x = dq[0][0], dq[0][1]

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds:
                if A[ny][nx] == 0:
                    dq.append([ny,nx])
                    A[ny][nx] = A[y][x] + 1
                if first and A[ny][nx] == 1:
                    touchWalls.append([ny,nx])
        dq.popleft()

    if first:
        return (A[n-1][m-1] - 1, touchWalls)
    else:
        return A[n-1][m-1] - 1

minPath, walls = grid_bfs([0,0],True)
if minPath == -1:
    minPath = 999999

for y,x in walls:
    L[y][x] = 0
    path = grid_bfs([0,0],False)
    if path != -1:
        minPath = min(grid_bfs([0,0],False), minPath)
    L[y][x] = 1

if minPath != 999999:
    print(minPath)
else:
    print(-1)