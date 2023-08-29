import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

def dijkstra():
    hq = [(0,1)]
    cost = [int(2e4)] * (n+1)
    cost[1] = 0
    trace = [[1] for _ in range(n+1)]

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for nv,nw in graph[v]:
            newCost = cost[v]+nw
            if newCost < cost[nv]:
                cost[nv] = newCost
                heapq.heappush(hq,(newCost,nv))
                trace[nv] = trace[v] + [nv]

    return trace

path = dijkstra()
edges = set()

for i in path[2:]:
    for j in range(len(i)-1):
        edges.add((i[j],i[j+1]))

print(len(edges))
for i in edges:
    print(*i)