import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
L = []
for _ in range(n):
    line = list(map(int,input().rstrip()))
    L.append(line)

cnt = 0
numlist = []
def grid_bfs(L,start):
    global cnt
    global numlist
    aptnum = 0
    dq = deque() #checklist

    if L[start[0]][start[1]] == 0:
        return L
    else:
        dq.append(start)
        L[start[0]][start[1]] = 0

    while dq:
        y,x = dq[0][0], dq[0][1]

        near = [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]
        for i in near:
            inbounds = (-1 < i[0] < n) and (-1 < i[1] < n)
            if inbounds:
                if L[i[0]][i[1]] == 1:
                    dq.append(i)
                    L[i[0]][i[1]] = 0
        dq.popleft()
        aptnum += 1
    cnt += 1
    numlist.append(aptnum)
    return L

for i in range(n):
    for j in range(n):
        L = grid_bfs(L,[i,j])

print(cnt)
numlist.sort()
for i in numlist:
    print(i)