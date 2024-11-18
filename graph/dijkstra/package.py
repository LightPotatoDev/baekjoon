import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = [(0,start)]
    cost = [int(1e10)] * (n+1)
    cost[start] = 0
    trace = [0]*(n+1)

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for nw,nv in graph[v]:
            newCost = cost[v]+nw
            if newCost < cost[nv]:
                trace[nv] = v
                cost[nv] = newCost
                heapq.heappush(hq,(newCost,nv))

    return trace

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,p = map(int,input().split())
    graph[u].append((p,v))
    graph[v].append((p,u))

chart = [['-']*n for _ in range(n)]
for i in range(1,n+1):
    trace = dijkstra(i)
    for j in range(1,n+1):
        if i != j:
            chart[j-1][i-1] = trace[j]

for i in chart:
    print(*i)
