import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
yi,xi,yf,xf = map(lambda x:int(x)-1,input().split())
L = []
for i in range(n):
    line = list(input().rstrip())
    for j in range(m):
        if i == yi and j == xi:
            line[j] = 0
        if i == yf and j == xf:
            line[j] = 1
    L.append(list(map(int,line)))

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def grid_01bfs(yi,xi,yf,xf):
    dq = deque()
    dq.append([yi,xi])

    while dq:
        p = dq.popleft()
        y,x = p[0], p[1]

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if not ((0 <= ny < n) and (0 <= nx < m)):
                continue

            if L[ny][nx] == 0:
                dq.appendleft([ny,nx])
                L[ny][nx] = L[y][x]
            elif L[ny][nx] == 1:
                dq.append([ny,nx])
                L[ny][nx] = L[y][x] + 1

    return L[yf][xf]+1

print(grid_bfs(yi,xi,yf,xf))