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

n = int(input())
a,b,c = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,l = map(int,input().split())
    graph[s].append((l,e))
    graph[e].append((l,s))

costs = []
for i in [a,b,c]:
    costs.append(dijkstra(i))

ans = -1
ansDist = -1
for i in range(1,n+1):
    dist = min([costs[j][i] for j in range(3)])
    if dist > ansDist:
        ans = i
        ansDist = dist
print(ans)