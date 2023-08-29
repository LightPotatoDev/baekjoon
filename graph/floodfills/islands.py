import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]

def grid_bfs(L):

    def fill(r,c):
        dq = deque([(r,c)])

        while dq:
            y,x = dq.popleft()
            L[y][x] = 0
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                inbounds = 0 <= ny < h and 0 <= nx < w
                if inbounds and L[ny][nx] == 1:
                    dq.append((ny,nx))
                    L[ny][nx] = 0

    area = 0
    for i in range(h):
        for j in range(w):
            if L[i][j] == 1:
                area += 1
                fill(i,j)

    return area

while True:
    grid = []
    w,h = map(int,input().split())
    if w == 0:
        break
    for i in range(h):
        grid.append(list(map(int,input().rstrip().split())))
    print(grid_bfs(grid))