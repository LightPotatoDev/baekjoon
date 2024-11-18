import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def grid_bfs(yi,xi):
    dq = deque([[yi,xi]])
    A[yi][xi] = areaID
    area = [[yi,xi]]

    while dq:
        y,x = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if not ((0 <= ny < n) and (0 <= nx < n)):
                continue

            if (l <= abs(L[y][x] - L[ny][nx]) <= r) and A[ny][nx] == 0:
                A[ny][nx] = areaID
                area.append([ny,nx])
                dq.append([ny,nx])

    if len(area) > 1:
        areas.append(area.copy())


n,l,r = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]

ans = 0
while True:
    A = [[0]*n for _ in range(n)]
    areaID = 1
    areas = []
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:
                grid_bfs(i,j)
                areaID += 1

    if len(areas) == 0:
        break
    ans += 1

    for a in areas:
        s = sum([L[y][x] for y,x in a])
        for y,x in a:
            L[y][x] = s // len(a)

print(ans)