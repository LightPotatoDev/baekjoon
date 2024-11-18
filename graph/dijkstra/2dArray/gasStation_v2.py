import sys
import heapq
input = sys.stdin.readline
COSTRANGE = 5

def dijkstra(start,end):
    oil = oilCost[start]
    hq = [(0,oil,start)]
    cost = [[int(1e10)]*(n+1) for _ in range(COSTRANGE+1)]
    cost[oil][start] = 0

    while hq:
        w,o,v = heapq.heappop(hq)
        if cost[o][v] < w:
            continue
        for nw,nv in graph[v]:
            newCost = cost[o][v] + nw*o
            if newCost < cost[o][nv]:
                cost[o][nv] = newCost
                cost[oilCost[nv]][nv] = min(cost[oilCost[nv]][nv],newCost)
                heapq.heappush(hq,(newCost,min(o,oilCost[nv]),nv))

    return cost

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
oilCost = [0]+list(map(int,input().split()))
for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))

L = dijkstra(1,n)
print(min([L[i][n] for i in range(COSTRANGE+1)]))