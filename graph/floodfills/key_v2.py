import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dy = [-1,0,0,1]
dx = [0,-1,1,0]

def unlock(k):
    for y,x in doors[ord(k)-97]:
        L[y][x] = "."
    doors[ord(k)-97] = []

def walkable(y,x):
    return L[y][x] == '.' or L[y][x] == '$' or L[y][x].islower()

def grid_bfs(yi,xi):
    global cnt

    dq = deque([[yi,xi]])
    A = [[0]*m for _ in range(n)]
    A[yi][xi] = 1
    while dq:
        y,x = dq.popleft()
        if L[y][x] == "$":
            cnt += 1
            L[y][x] = '.'
        elif L[y][x].islower():
            unlock(L[y][x])
            gotKey = 3
            L[y][x] = '.'

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds and walkable(ny,nx) and A[ny][nx] == 0:
                A[ny][nx] = 1
                dq.append([ny,nx])

for _ in range(T):
    n,m = map(int,input().split())
    L = []
    doors = [[] for _ in range(26)]
    for i in range(n):
        row = list(input().rstrip())
        for j,x in enumerate(row):
            if x.isupper():
                doors[ord(x)-65].append([i,j])
        L.append(row)

    K = list(input().rstrip())
    if K[0] == '0':
        K = []

    while K:
        p = K.pop()
        unlock(p)

    edge = []
    for i in range(m-1):
        edge.append([0,i])
        edge.append([n-1,i+1])
    for i in range(n-1):
        edge.append([i,m-1])
        edge.append([i+1,0])

    cnt = 0
    gotKey = 3
    while True:
        for y,x in edge:
            if walkable(y,x):
                grid_bfs(y,x)

        gotKey -= 1
        if gotKey == 0:
            break

    print(cnt)