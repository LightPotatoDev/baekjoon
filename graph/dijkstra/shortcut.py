import sys
import heapq
input = sys.stdin.readline

n,d = map(int,input().split())

graph = [[] for _ in range(d+1)]

for _ in range(n):
    s,e,w = map(int,input().split())
    if e <= d and e-s > w:
        graph[s].append((e,w))
for i in range(d):
    graph[i].append((i+1,1))

def dijkstra(start):
    hq = [(0,start)]
    cost = [int(2e4)] * (d+1)
    cost[start] = 0

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for nv,nw in graph[v]:
            newCost = cost[v]+nw
            if newCost < cost[nv]:
                cost[nv] = newCost
                heapq.heappush(hq,(newCost,nv))

    return cost[d]

print(dijkstra(0))