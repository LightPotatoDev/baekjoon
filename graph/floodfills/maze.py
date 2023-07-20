import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
L = []
for _ in range(n):
    line = list(map(int,input().rstrip()))
    L.append(line)

def grid_bfs(L,start):
    dq = deque() #checklist
    dq.append(start)
    L[0][0] = 2
    while dq:
        y,x = dq[0][0], dq[0][1]

        near = [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]
        for i in near:
            inbounds = (-1 < i[0] < n) and (-1 < i[1] < m)
            if inbounds:
                if L[i[0]][i[1]] == 1:
                    dq.append(i)
                    L[i[0]][i[1]] = L[y][x] + 1
        dq.popleft()
    return L[n-1][m-1] - 1

print(grid_bfs(L,[0,0]))