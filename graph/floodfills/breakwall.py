import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
L = []
for _ in range(n):
    line = list(map(int,input().rstrip()))
    L.append(line)

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def grid_bfs(start):
    dq = deque()
    dq.append(start)
    L[0][0] = 2
    while dq:
        y,x = dq[0][0], dq[0][1]

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds:
                if L[ny][nx] == 0:
                    dq.append([ny,nx])
                    L[ny][nx] = L[y][x] + 1
        dq.popleft()

    return L[n-1][m-1] - 1

print(grid_bfs([0,0]))