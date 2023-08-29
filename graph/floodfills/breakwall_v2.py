import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = []
L = []
for _ in range(n):
    row = list(map(int,input().rstrip()))
    board.append(row[:])
    L.append(row[:])
for i in range(n):
    for j in range(m):
        L[i][j] = [L[i][j],0]

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def grid_bfs(start):
    dq = deque()
    dq.append(start)
    L[0][0][0] = 2
    while dq:
        y,x,state = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds:
                if state == 0:
                    if L[ny][nx][0] == 0:
                        dq.append([ny,nx,0])
                        L[ny][nx][0] = L[y][x][0] + 1
                        L[ny][nx][1] = 0

                    elif L[ny][nx][0] == 1:
                        dq.append([ny,nx,1])
                        L[ny][nx][0] = L[y][x][0] + 1
                        L[ny][nx][1] = 1

                    elif L[ny][nx][1] == 1 and [ny,nx] != [n-1,m-1] and board[ny][nx] == 0:
                        dq.append([ny,nx,0])
                        L[ny][nx][0] = L[y][x][0] + 1
                        L[ny][nx][1] = 0
                else:
                    if L[ny][nx][0] == 0:
                        dq.append([ny,nx,1])
                        L[ny][nx][0] = L[y][x][0] + 1
                        L[ny][nx][1] = 1

    return L[n-1][m-1][0] - 1

print(grid_bfs([0,0,0]))