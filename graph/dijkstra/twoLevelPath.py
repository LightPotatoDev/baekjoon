import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = [(0,start)]
    cost = [int(5e13)] * (n+1)
    cost[start] = 0

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for nw,nv in graph[v]:
            newCost = cost[v]+nw
            if newCost < cost[nv]:
                cost[nv] = newCost
                heapq.heappush(hq,(newCost,nv))

    return cost

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
x,z = map(int,input().split())
p = int(input())
midpoint = list(map(int,input().split()))

fromS = dijkstra(x)
fromE = dijkstra(z)
ans = int(5e13)
for y in midpoint:
    ans = min(ans, fromS[y]+fromE[y])
if ans >= int(5e13):
    print(-1)
else:
    print(ans)
