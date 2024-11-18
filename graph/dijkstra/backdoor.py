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

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
reachable = list(map(int,input().split()))
reachable[n-1] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    if (reachable[a] == 0 and reachable[b] == 0):
        graph[a].append((c,b))
        graph[b].append((c,a))

ans = dijkstra(0,n-1)
if ans == int(1e10):
    ans = -1
print(ans)