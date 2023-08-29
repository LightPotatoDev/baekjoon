import sys
input = sys.stdin.readline

row,col,m = map(int,input().split())
L = [[(0,0,0) for _ in range(col)] for _ in range(row)]

for _ in range(m):
    r,c,s,d,z = map(int,input().split())
    L[r-1][c-1] = (s,d,z)

def calcDist(y,x,s,d):
    vertical = (d-1) // 2 == 0
    if vertical:
        s = s % ((row-1)*2)
    else:
        s = s % ((col-1)*2)

    while s > 0:
        if d == 1 or d == 2:
            if d == 1 and y == 0:
                d = 2
            elif d == 2 and y == row - 1:
                d = 1
            y += 1 if d == 2 else -1
        elif d == 3 or d == 4:
            if d == 3 and x == col - 1:
                d = 4
            elif d == 4 and x == 0:
                d = 3
            x += 1 if d == 3 else -1
        s -= 1

    return (y,x,d)

def moveShark(y,x):
    spd,dir,size = L[y][x]
    L[y][x] = (0,0,0)
    ny,nx,nd = calcDist(y,x,spd,dir)
    return (ny,nx,spd,nd,size)

def catchShark(c):
    for r in range(row):
        if L[r][c][1] != 0:
            z = L[r][c][2]
            L[r][c] = (0,0,0)
            return z
    return 0

score = 0

for i in range(col):
    score += catchShark(i)
    A = []
    for r in range(row):
        for c in range(col):
            if L[r][c][1] != 0:
                A.append(moveShark(r,c))

    for r,c,s,d,z in A:
        occupying = L[r][c][2]
        if occupying < z:
            L[r][c] = (s,d,z)
print(score)
