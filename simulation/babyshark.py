import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
L = []
sharkY = 0
sharkX = 0
for i in range(n):
    line = list(map(int,input().rstrip().split()))
    if 9 in line:
        sharkY = i
        sharkX = line.index(9)
    L.append(line)
L[sharkY][sharkX] = 0

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def grid_bfs(yi,xi,grid):
    dq = deque()
    dq.append([yi,xi])
    grid[yi][xi] = 3
    targetPos = []
    #0: empty / 1: edible fish / 2: wall / 3+: path
    while dq:
        y,x = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < n)
            if inbounds and grid[ny][nx] <= 1:
                dq.append([ny,nx])
                if grid[ny][nx] == 1:
                    targetPos.append([grid[y][x] - 2, ny, nx])
                grid[ny][nx] = grid[y][x] + 1

    if targetPos:
        targetPos.sort(key = lambda x:(x[0],x[1],x[2]))
        return targetPos[0]
    else:
        return [-1,-1,-1]

totalTime = 0
level = 2
exp = 0
while True:
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if 1 <= L[i][j] <= level-1:
                A[i][j] = 1
            if L[i][j] > level:
                A[i][j] = 2

    time,newY,newX = grid_bfs(sharkY, sharkX, A)

    if time == -1:
        break
    else:
        totalTime += time
        sharkY = newY
        sharkX = newX
        exp += 1
        if exp == level:
            level += 1
            exp = 0
        L[sharkY][sharkX] = 0

print(totalTime)
