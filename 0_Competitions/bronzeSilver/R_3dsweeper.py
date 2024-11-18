import sys
input = sys.stdin.readline
from itertools import product

r,c,h = map(int,input().split())

L = [[list(input().rstrip()) for _ in range(r)] for _ in range(h)] #[h][r][c]

def findmine(z,y,x):
    mines = 0
    diff = product([-1,0,1],repeat=3)
    for dz,dy,dx in diff:
        nz,ny,nx = z+dz,y+dy,x+dx
        inbounds = 0 <= nz < h and 0 <= ny < r and 0 <= nx < c
        if inbounds and L[nz][ny][nx] == "*":
            mines += 1

    return mines%10


for k in range(h):
    for i in range(r):
        for j in range(c):
            if L[k][i][j] == ".":
                L[k][i][j] = findmine(k,i,j)

for k in L:
    for i in k:
        print(''.join(map(str,i)))