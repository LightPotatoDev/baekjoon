import sys
import math
import heapq
input = sys.stdin.readline

n,m,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
graphR = [[] for _ in range(n+1)]
costs = []

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    graphR[e].append((s,w))

def dijkstra(start,g):
    hq = [(0,start)]
    cost = [math.inf] * (n+1)
    cost[start] = 0

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for nv,nw in g[v]:
            newCost = cost[v]+nw
            if newCost < cost[nv]:
                cost[nv] = newCost
                heapq.heappush(hq,(newCost,nv))

    return cost

costs.append(dijkstra(x,graph)[1:])
costs.append(dijkstra(x,graphR)[1:])

maxCost = 0
for i in range(n):
    maxCost = max(maxCost, costs[0][i] + costs[1][i])
print(maxCost)

#1-x-1이나 x-1-x나 똑같다
#목적지로부터 다익스트라를 돌리면 돌리는 횟수를 줄일 수 있음