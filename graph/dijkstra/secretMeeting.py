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

    return sum([cost[i] for i in friends])

T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))

    k = int(input())
    friends = list(map(int,input().split()))

    minCost = int(1e10)
    ans = 0
    for i in range(1,n+1):
        cost = dijkstra(i)
        if cost < minCost:
            minCost = cost
            ans = i
    print(ans)