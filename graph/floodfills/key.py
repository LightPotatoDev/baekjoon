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

def grid_bfs(yi,xi):
    dq = deque([[yi,xi]])
    A = [[0]*m for _ in range(n)]
    A[yi][xi] = 1
    while dq:
        y,x = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if not inbounds:
                return True
            if L[ny][nx] != "*" and (not L[ny][nx].isupper()) and A[ny][nx] == 0:
                A[ny][nx] = 1
                dq.append([ny,nx])

    return False

def keyEscape():
    flag = False

    K = keys.copy()
    while K:
        y,x,k = K.popleft()
        if not doors[ord(k)-97]:
            keys.popleft()
            continue
        if grid_bfs(y,x):
            L[y][x] = "."
            unlock(k)
            flag = True

    return flag

for _ in range(T):
    n,m = map(int,input().split())
    L = []
    keys  = deque([]) #(y,x,type)
    doors = [[] for _ in range(26)]
    files = []
    for i in range(n):
        row = list(input().rstrip())
        for j,x in enumerate(row):
            if x.isupper():
                doors[ord(x)-65].append([i,j])
            elif x.islower():
                keys.append([i,j,x])
            elif x == "$":
                files.append([i,j])
        L.append(row)

    K = list(input().rstrip())
    if K[0] == '0':
        K = []

    while K:
        p = K.pop()
        unlock(p)

    while True:
        if not keyEscape():
            break

    cnt = 0
    for y,x in files:
        if grid_bfs(y,x):
            cnt += 1
            L[y][x] = '.'
    print(cnt)
    for i in L:
        print(''.join(i))