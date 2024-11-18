import sys
import heapq
input = sys.stdin.readline

def dijkstra(yi,xi,yf,xf):
    hq = [(0,yi,xi)]
    cost = [[int(1e6)]*m for _ in range(n)]
    cost[yi][xi] = grid[yi][xi]

    while hq:
        w,y,x = heapq.heappop(hq)
        if cost[y][x] < w:
            continue
        for nw,ny,nx in graph[y][x]:
            newCost = cost[y][x]+nw
            if newCost < cost[ny][nx]:
                cost[ny][nx] = newCost
                heapq.heappush(hq,(newCost,ny,nx))

    return cost[yf][xf]

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
graph = [[[] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == -1:
            continue
        if i > 0 and grid[i-1][j] != -1:
            graph[i][j].append((grid[i-1][j],i-1,j))
        if i < n-1 and grid[i+1][j] != -1:
            graph[i][j].append((grid[i+1][j],i+1,j))
        if j > 0 and grid[i][j-1] != -1:
            graph[i][j].append((grid[i][j-1],i,j-1))
        if j < m-1 and grid[i][j+1] != -1:
            graph[i][j].append((grid[i][j+1],i,j+1))

ans = dijkstra(0,0,n-1,m-1)
if ans == int(1e6):
    print(-1)
else:
    print(ans)

