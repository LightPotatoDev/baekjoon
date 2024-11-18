import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,end):
    hq = [(0,start)]
    cost = [int(1e10)] * (n+1)
    cost[start] = 0
    trace = [[] for _ in range(n+1)]

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for nw,nv in graph[v]:
            newCost = cost[v]+nw
            if newCost == cost[nv]:
                trace[nv].append(v)
            if newCost < cost[nv]:
                cost[nv] = newCost
                trace[nv] = []
                trace[nv].append(v)
                heapq.heappush(hq,(newCost,nv))

    return cost[end],trace

while True:
    n,m = map(int,input().split())

    if n == 0:
        break
    s,d = map(int,input().split())
    graph = [[0]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        u,v,p = map(int,input().split())
        graph[u][v] = p

    for i in graph:
        print(i)
    cost, trace = dijkstra(s,d)
    toDelete = [[i,d] for i in trace[d]]
    while toDelete:
        st,ed = toDelete.pop()
        toDelete.extend([i,ed] for i in trace[ed])
        graph[st].remove(ed)
    print(graph)


