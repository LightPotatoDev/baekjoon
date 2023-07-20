import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
L = []
viraPos = []
blankPos = []

wallN = 0
virusN = 0
for i in range(n):
    line = list(map(int,input().split()))
    for j,x in enumerate(line):
        if x == 2:
            viraPos.append([i,j])
            virusN += 1
        elif x == 1:
            wallN += 1
        else:
            blankPos.append([i,j])

    L.append(line)

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def grid_bfs(A,start):
    dq = deque(start)
    virN = virusN

    while dq:
        p = dq.popleft()
        y,x = p[0], p[1]

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds and A[ny][nx] == 0:
                dq.appendleft([ny,nx])
                virN += 1
                A[ny][nx] = 2

    return n*m - wallN - virN - 3

safe = 0
comb = combinations(blankPos,3)
for c in comb:
    A = copy.deepcopy(L)
    for y,x in c:
        A[y][x] = 1
    safe = max(safe,grid_bfs(A,viraPos))

print(safe)
