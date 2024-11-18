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

T = int(input())
for _ in range(T):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((s,a))

    L = dijkstra(c)
    infected = n+1
    for i in range(n+1):
        if L[i] == int(1e10):
            infected -= 1
            L[i] = -1

    print(infected, max(L))

