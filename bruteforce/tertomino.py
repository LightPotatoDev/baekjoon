import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

def boardadd(ny,nx,y,x):
    total = 0
    for i in range(4):
        ypos = y+ny[i]
        xpos = x+nx[i]
        if ypos < 0 or ypos >= n or xpos < 0 or xpos >= m:
            return 0
        else:
            total += board[ypos][xpos]
    return total

sums = set()
def tetristime(ny,nx):
    global sums
    for i in range(n):
        for j in range(m):
            sums.add(boardadd(ny,nx,i,j))

dy = [[0,0,0,0],[0,0,1,1],[0,1,2,2],[0,1,2, 2],[0,1,1,2],[0,1, 1, 2],[0,0,0,1]]
dx = [[0,1,2,3],[0,1,0,1],[0,0,0,1],[0,0,0,-1],[0,0,1,1],[0,0,-1,-1],[0,1,2,1]]
#       I           O          L        J          S           Z          T

for i in range(7):
    for _ in range(4):
        tetristime(dy[i],dx[i])
        dy[i],dx[i] = dx[i],list(map(lambda x:-x,dy[i]))

print(max(sums))