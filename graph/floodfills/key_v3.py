import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dy = [-1,0,0,1]
dx = [0,-1,1,0]

def unlock(k):
    for y,x in doors[ord(k)-97]:
        L[y][x] = "."
    for y,x in keys[ord(k)-97]:
        L[y][x] = "."
    keys[ord(k)-97] = []
    doors[ord(k)-97] = []

def grid_bfs(yi,xi):
    global cnt
    global gotThing

    dq = deque([[yi,xi]])
    A[yi][xi] = 1
    obtainable = False
    items = []
    while dq:
        y,x = dq.popleft()
        if L[y][x].islower() or L[y][x] == "$":
            items.append((y,x,L[y][x]))

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if not inbounds:
                obtainable = True
            elif L[ny][nx] != "*" and (not L[ny][nx].isupper()) and A[ny][nx] == 0:
                A[ny][nx] = 1
                dq.append([ny,nx])

    if obtainable:
        gotThing = True
        for y,x,i in items:
            if i == "$":
                cnt += 1
            else:
                unlock(i)
            L[y][x] = "."

for _ in range(T):

    #initialize
    n,m = map(int,input().split())
    L = []
    keys  = [[] for _ in range(26)]
    doors = [[] for _ in range(26)]
    for i in range(n):
        row = list(input().rstrip())
        for j,x in enumerate(row):
            if x.isupper():
                doors[ord(x)-65].append([i,j])
            elif x.islower():
                keys[ord(x)-97].append([i,j])
        L.append(row)

    #keys already got
    K = list(input().rstrip())
    if K[0] == '0':
        K = []
    while K:
        p = K.pop()
        unlock(p)

    #bfs time
    cnt = 0
    while True:
        A = [[0]*m for _ in range(n)]
        gotThing = False
        for i in range(n):
            for j in range(m):
                if (L[i][j].islower() or L[i][j] == "$") and A[i][j] == 0:
                    grid_bfs(i,j)
        if gotThing == False:
            break

    print(cnt)