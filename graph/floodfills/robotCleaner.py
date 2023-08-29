import sys
from collections import deque
from copy import deepcopy
from itertools import permutations
input = sys.stdin.readline

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def grid_bfs(yi,xi):
    A = deepcopy(L)
    A[yi][xi] = 0
    dq = deque([[yi,xi]])

    while dq:
        y,x = dq.popleft()
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds and A[ny][nx] != "x" and isinstance(A[ny][nx], str):
                A[ny][nx] = A[y][x] + 1
                dq.append([ny,nx])

    G = []
    for i in range(len(Dust)):
        y,x = Dust[i]
        G.append(A[y][x])
    return G

while True:
    m,n = map(int,input().split())
    if m == 0:
        break

    Dust = []
    Cleaner = []
    L = []
    for i in range(n):
        row = list(input().rstrip())
        for j,x in enumerate(row):
            if x == "*":
                Dust.append([i,j])
            elif x == "o":
                Cleaner.append([i,j])
        L.append(row)

    graph = [[] for _ in range(len(Dust)+1)]
    for i,pos in enumerate(Cleaner+Dust):
        yi,xi = pos
        graph[i] = [0]+grid_bfs(yi,xi)

    cleanable = True
    for x in graph[0]:
        if x == "*":
            cleanable = False
    if cleanable == False:
        print(-1)
        continue

    perm = permutations(range(1,len(Dust)+1), len(Dust))
    minDist = int(1e9)
    for p in perm:
        dist = 0
        a = 0
        for b in p:
            dist += graph[a][b]
            a = b
        minDist = min(minDist,dist)
    print(minDist)
