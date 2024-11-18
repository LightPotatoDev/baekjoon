import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
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

    return cost

def dijkstra_wolf(start):
    FAST = 0
    SLOW = 1
    hq = [(0,start,FAST)]
    cost = [[int(1e10),int(1e10)] for _ in range(n+1)]
    cost[start][0] = 0

    while hq:
        w,v,mode = heapq.heappop(hq)
        if cost[v][mode] < w:
            continue
        for nw,nv in graph[v]:
            newCost = 0
            if mode == FAST:
                newCost = cost[v][mode] + nw//2
            if mode == SLOW:
                newCost = cost[v][mode] + nw*2

            if newCost < cost[nv][1-mode]:
                cost[nv][1-mode] = newCost
                heapq.heappush(hq,(newCost,nv,1-mode))

    return cost

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,p = map(int,input().split())
    p *= 2
    graph[u].append((p,v))
    graph[v].append((p,u))

foxResult = dijkstra(1)
wolfResult = [min(i) for i in dijkstra_wolf(1)]
ans = 0
for i in range(1,n+1):
    if foxResult[i] < wolfResult[i]:
        ans += 1
print(ans)