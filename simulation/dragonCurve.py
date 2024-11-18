n = int(input())
SIZE = 100
grid = [[0]*(SIZE+1) for _ in range(SIZE+1)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]

def rotate(points,center):
    P = points[:]
    cy,cx = center

    for y,x in points:
        oldY,oldX = y,x
        y -= cy
        x -= cx
        y,x = x,y
        x *= -1
        y += cy
        x += cx
        if y != oldY or x != oldX:
            P.append((y,x))

    return P

for _ in range(n):
    x,y,d,g = map(int,input().split())
    ny = y+dy[d]
    nx = x+dx[d]
    points = [(y,x),(ny,nx)]
    center = (ny,nx)
    for _ in range(g):
        points = rotate(points,center)
        center = rotate([(y,x)],center)[1]

    for i,j in points:
        grid[i][j] = 1

ans = 0
for i in range(SIZE):
    for j in range(SIZE):
        if grid[i][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j] == 1 and grid[i+1][j+1]==1:
            ans += 1
print(ans)