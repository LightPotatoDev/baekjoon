import sys
import heapq
input = sys.stdin.readline

def dijkstra(yi,xi):
    hq = [(0,yi,xi)]
    cost = [[int(1e10)]*(n+1) for _ in range(n+1)]
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

    return cost

n,m = map(int,input().split())
graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
oilCost = [0]+list(map(int,input().split()))
for _ in range(m):
    a,b,w = map(int,input().split())
    for i in range(1,n+1):
        graph[i][a].append((w*oilCost[i],i,b))
        graph[i][b].append((w*oilCost[i],i,a))
        if oilCost[a] < oilCost[i]:
            graph[i][a].append((0,a,a))

L = dijkstra(1,1)
print(min([L[i][n] for i in range(1,n+1)]))