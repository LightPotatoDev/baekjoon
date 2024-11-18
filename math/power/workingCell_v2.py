import sys
input = sys.stdin.readline
from copy import deepcopy

mod = int(1e9)+7
t,n,d = map(int,input().split())
gBase = [[[0]*n for _ in range(n)] for _ in range(t)]
gExp  = [[[0]*n for _ in range(n)] for _ in range(35)]
for i in range(t):
    m = int(input())
    for j in range(m):
        a,b,c = map(int,input().split())
        gBase[i][a-1][b-1] = c

def moveCell(G):
    global cellMap
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for row in range(n):
                A[row][j] = (A[row][j] + (cellMap[row][i] * G[i][j]) % mod) % mod
    cellMap = deepcopy(A)

def printCellMap():
    for row in cellMap:
        print(*row)

cellMap = [[0]*n for _ in range(n)]
for i in range(n):
    cellMap[i][i] = 1
for step in range(min(t,d)):
    moveCell(gBase[step])

curStep = min(t,d)
stepSize = t
exp = 0

while curStep*2 <= d:
    curStep *= 2
    stepSize *= 2
    gExp[exp] = deepcopy(cellMap)
    moveCell(gExp[exp])
    exp += 1

while stepSize > t:
    stepSize //= 2
    exp -= 1
    if (curStep + stepSize) <= d:
        moveCell(gExp[exp])
        curStep += stepSize

for i in range(d-curStep):
    moveCell(gBase[i])

printCellMap()
