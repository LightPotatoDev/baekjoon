import sys
input = sys.stdin.readline

r,c = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(r)]
flag = 1

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def checkNear(y,x):
    for i in range(4):
        ny,nx = y+dy[i], x+dx[i]
        inbounds = (0 <= ny < r) and (0 <= nx < c)
        if inbounds:
            if grid[ny][nx] == 'W':
                return 0
    return 1


for i in range(r):
    for j in range(c):
        if grid[i][j] == 'S' and flag == 1:
            flag = checkNear(i,j)
        if grid[i][j] == '.':
            grid[i][j] = 'D'

print(flag)
if flag == 1:
    for i in range(r):
        print(''.join(grid[i]))
