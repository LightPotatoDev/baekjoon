import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,end,delS,delE):
    hq = [(0,start)]
    cost = [int(1e10)] * (n+1)
    cost[start] = 0
    trace = [[] for _ in range(n+1)]

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for nw,nv in graph[v]:
            if (v == delS and nv == delE) or (v == delE and nv == delS):
                continue
            newCost = cost[v]+nw
            if newCost == cost[nv]:
                trace[nv].append(v)
            if newCost < cost[nv]:
                cost[nv] = newCost
                trace[nv] = []
                trace[nv].append(v)
                heapq.heappush(hq,(newCost,nv))

    return cost[end],trace

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
delete = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u,v,p = map(int,input().split())
    graph[u].append((p,v))
    graph[v].append((p,u))

oldC, trace = dijkstra(1,n,0,0)

toDelete = [[i,n] for i in trace[n]]
while toDelete:
    st,ed = toDelete.pop()
    if delete[st][ed] == 0:
        toDelete.extend([[i,st] for i in trace[st]])
        delete[st][ed] = 1

delay = -1
for i in range(1,n+1):
    for j in range(1,n+1):
        if delete[i][j] == 1:
            newC, trace = dijkstra(1,n,i,j)
            if newC >= int(1e10):
                print(-1)
                exit()
            delay = max(delay,newC-oldC)

print(delay)
