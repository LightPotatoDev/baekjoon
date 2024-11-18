import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
graph = [[[] for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '\\':
            graph[i][j].append((0,i+1,j+1))
            graph[i+1][j+1].append((0,i,j))
            graph[i][j+1].append((1,i+1,j))
            graph[i+1][j].append((1,i,j+1))
        else:
            graph[i][j].append((1,i+1,j+1))
            graph[i+1][j+1].append((1,i,j))
            graph[i][j+1].append((0,i+1,j))
            graph[i+1][j].append((0,i,j+1))

def _01bfs(yi,xi,yf,xf):
    dq = deque()
    dq.append([yi,xi])
    cost = [[int(1e7)]*(m+1) for _ in range(n+1)]
    cost[yi][xi] = 0

    while dq:
        y,x = dq.popleft()

        for nc,ny,nx in graph[y][x]:
            if cost[y][x] + nc < cost[ny][nx]:
                cost[ny][nx] = cost[y][x] + nc
                if nc == 0:
                    dq.appendleft([ny,nx])
                elif nc == 1:
                    dq.append([ny,nx])

    return cost[yf][xf]

ans = _01bfs(0,0,n,m)
if ans == int(1e7):
    print('NO SOLUTION')
else:
    print(ans)