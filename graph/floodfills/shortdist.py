import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
me = [0,0]
L = []
for i in range(n):
    line = list(input().rstrip().split())
    if '2' in line:
        me = [i,line.index('2')]
    L.append(line)

def grid_bfs(L,start):
    dq = deque() #checklist
    dq.append(start)
    L[start[0]][start[1]] = 0
    while dq:
        y,x = dq[0][0], dq[0][1]

        near = [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]
        for i in near:
            inbounds = (-1 < i[0] < n) and (-1 < i[1] < m)
            if inbounds:
                if L[i[0]][i[1]] == '1':
                    dq.append(i)
                    L[i[0]][i[1]] = int(L[y][x]) + 1
        dq.popleft()

    for i in L:
        for j,x in enumerate(i):
            if x == '1':
                i[j] = -1
    return L

L = grid_bfs(L,me)
for i in L:
    print(' '.join(map(str,i)))