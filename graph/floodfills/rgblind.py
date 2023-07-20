import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
L = []
L2 = []
for _ in range(n):
    line = list(input().rstrip())
    L.append(line)
    line = list(map(lambda x: x.replace("G","R"),line))
    L2.append(line)

cnt = 0
dy = [-1,0,0,1]
dx = [0,-1,1,0]

def grid_bfs(L,start):
    global cnt
    mycolor = ""
    dq = deque() #checklist

    if L[start[0]][start[1]] == 0:
        return L
    else:
        dq.append(start)
        mycolor = L[start[0]][start[1]]
        L[start[0]][start[1]] = 0

    while dq:
        y,x = dq[0][0], dq[0][1]
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if (0 <= ny < n) and (0<= nx < n):
                if L[ny][nx] == mycolor:
                    dq.append([ny,nx])
                    L[ny][nx] = 0
        dq.popleft()
    cnt += 1
    return

for i in range(n):
    for j in range(n):
        grid_bfs(L,[i,j])
print(cnt, end=" ")

cnt = 0
for i in range(n):
    for j in range(n):
        grid_bfs(L2,[i,j])

print(cnt)