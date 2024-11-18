from collections import deque

h,w = map(int,input().split())
L = [list(input()) for _ in range(h)]

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def grid_bfs(yi,xi):
    dq = deque([[yi,xi]])
    L[yi][xi] = 1
    size = 0
    isPoly = True

    while dq:
        y,x = dq.popleft()
        size += 1

        if y == 0 or y == h-1 or x == 0 or x == w-1:
            isPoly = False

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < h) and (0 <= nx < w)
            if inbounds and L[ny][nx] == '.':
                L[ny][nx] = 1
                dq.append([ny,nx])

    if isPoly:
        return size*2
    else:
        return 0

area = 0
for i in range(h):
    for j in range(w):
        if L[i][j] == "/" or L[i][j] == "\\":
            area += 1
        elif L[i][j] == ".":
            area += grid_bfs(i,j)

print(area//2)

"""
counter example:

../\..
.//\\.
//..\\
\\..//
.\\//.
..\/..
"""