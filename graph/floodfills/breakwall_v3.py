import sys
import copy
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
L = []
L2 = []
for _ in range(n):
    row = list(map(int,input().rstrip()))
    L.append(row)
    L2.append(row)

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def grid_bfs(start):
    dq = deque()
    dq.append(start)
    L[0][0] = 2
    while dq:
        y,x,state = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds:
                if L[ny][nx] == 0 and state == 0:
                    dq.append([ny,nx,0])
                    L[ny][nx] = L[y][x] + 1

                if L[ny][nx] == 1 and state == 0:
                    dq.append([ny,nx,1])
                    L2[ny][nx] = L[y][x] + 1

                if L[ny][nx] > 1 and state == 0:
                    dq.append([ny,nx,0])
                    L2[ny][nx] = L[y][x] + 1

                if L2[ny][nx] == 0 and state == 1:
                    dq.append([ny,nx,1])
                    L2[ny][nx] = L2[y][x] + 1

    for i in L:
        print(i)
    for i in L2:
        print(i)
    return (L[n-1][m-1] - 1, L2[n-1][m-1] - 1)

print(grid_bfs([0,0,0]))