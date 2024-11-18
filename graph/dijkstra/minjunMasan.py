import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,end):
    hq = [(0,start)]
    cost = [int(1e10)] * (n+1)
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

    return cost[end]

n,m,p = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

cost1 = dijkstra(1,n)
cost2 = dijkstra(1,p) + dijkstra(p,n)
if cost1 == cost2:
    print("SAVE HIM")
else:
    print("GOOD BYE")
