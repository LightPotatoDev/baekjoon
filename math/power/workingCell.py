import sys
input = sys.stdin.readline
from copy import deepcopy

t,n,d = map(int,input().split())
gBase = [[[] for _ in range(n)] for _ in range(t)]
gExp  = [[[] for _ in range(n)] for _ in range(35)]
for i in range(t):
    m = int(input())
    for j in range(m):
        a,b,c = map(int,input().split())
        gBase[i][a-1].append((c,b-1))

def moveCell(Map,G):
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for paths, toJ in G[j]:
                A[i][toJ] += Map[i][j] * paths
    return A

def printCellMap():
    for row in cellMap:
        print(*row)
    print('')

cellMap = [[0]*n for _ in range(n)]
for i in range(n):
    cellMap[i][i] = 1
for step in range(min(t,d)):
    newCellMap = moveCell(cellMap, gBase[step])
    cellMap = deepcopy(newCellMap)

curStep = min(t,d)
exp = 0
while curStep < d:
    if curStep*2 < d:
        curStep *= 2
        exp += 1
        newCellMap = moveCell(cellMap, )
printCellMap()

