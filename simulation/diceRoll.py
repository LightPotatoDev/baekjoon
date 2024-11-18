import sys
input = sys.stdin.readline

n,m,y,x,k = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
cmd = list(map(int,input().split()))
dice = [[0]*3 for _ in range(4)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def shift(dir):
    if dir == 1:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    elif dir == 2:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    elif dir == 3:
        t = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i+1][1]
        dice[3][1] = t
    elif dir == 4:
        t = dice[3][1]
        for i in range(3,0,-1):
            dice[i][1] = dice[i-1][1]
        dice[0][1] = t

def moveDice(dir):
    global y,x
    ny = y + dy[dir-1]
    nx = x + dx[dir-1]
    inbounds = (0 <= ny < n) and (0 <= nx < m)

    if not inbounds:
        return False

    shift(dir)
    y,x = ny,nx

    num = L[ny][nx]
    if (num == 0):
        L[ny][nx] = dice[3][1]
    else:
        L[ny][nx] = 0
        dice[3][1] = num

    return True

for i in cmd:
    if moveDice(i):
        print(dice[1][1])
##        for row in dice:
##            print(row)
##        print('')
