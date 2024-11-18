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

    if cost[end] == int(1e10):
        return -1
    else:
        return cost[end]

t,n,e = map(int,input().split())
f1,f2 = map(int,input().split())
L = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,l = map(int,input().split())
    graph[a].append((l,b))
    graph[b].append((l,a))

ans = 0
for i in L:
    ans += dijkstra(i,f1)
    ans += dijkstra(i,f2)
print(ans)