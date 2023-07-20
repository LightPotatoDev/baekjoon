import sys
import copy
input = sys.stdin.readline

r,c,t = map(int,input().split())
A = []
air1, air2 = 0,0
for i in range(r):
    line = list(map(int,input().split()))
    if line[0] == -1 and air1 == 0:
        air1 = i
        air2 = i+1
    A.append(line)

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def getAdj(y,x):
    adj = []
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        inbounds = 0 <= ny < r and 0 <= nx < c
        if inbounds and A[ny][nx] != -1:
            adj.append((ny,nx))
    return adj

def addMatrix(L,L2):
    for i in range(r):
        for j in range(c):
            L[i][j] += L2[i][j]
    return L

def spread():
    L = copy.deepcopy(A)
    L2 = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if A[i][j] > 0:
                adj = getAdj(i,j)
                amount = A[i][j] // 5
                L[i][j] -= amount * len(adj)

                for y,x in adj:
                    L2[y][x] += amount

    return addMatrix(L,L2)

def setWind():
    w = [[4] * c for _ in range(r)]
    #0:up  1:right  2:down  3:left

    for x in range(1,c-1):
        w[air1][x] = 1
        w[air2][x] = 1
    for x in range(1,c):
        w[0][x] = 3
        w[r-1][x] = 3
    for y in range(air1+1):
        w[y][0] = 2
        w[y][c-1] = 0
    for y in range(air2, r):
        w[y][0] = 0
        w[y][c-1] = 2
    w[0][c-1] = 3
    w[r-1][c-1] = 3

    return w

def blow():
    L = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            wState = wind[i][j]
            if wState != 4:
                ny = i + dy[wState]
                nx = j + dx[wState]
                L[ny][nx] = A[i][j]
            else:
                L[i][j] = A[i][j]

    L[air1][0] = -1
    L[air2][0] = -1
    return L

wind = setWind()

for _ in range(t):
    A = spread()
    A = blow()

print(sum([sum(i) for i in A]) + 2)
