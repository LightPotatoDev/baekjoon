import sys
import heapq
input = sys.stdin.readline

def dijkstra(yi,xi,yf,xf):
    hq = [(0,yi,xi)]
    cost = [[int(1e6)] * n for _ in range(n)]
    cost[yi][xi] = 0

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

n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
graph = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i < n-1:
            graph[i][j].append((max(0,grid[i+1][j]-grid[i][j]+1),i+1,j))
        if j < n-1:
            graph[i][j].append((max(0,grid[i][j+1]-grid[i][j]+1),i,j+1))

print(dijkstra(0,0,n-1,n-1))

