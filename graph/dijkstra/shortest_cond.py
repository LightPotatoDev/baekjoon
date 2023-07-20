import sys
import math
import heapq
input = sys.stdin.readline

n,edge = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(edge):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

mid1, mid2 = map(int,input().split())

def dijkstra(start,end):
    hq = [(0,start)] #가중치, 위치
    cost = [math.inf] * (n+1)
    cost[start] = 0

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for next in graph[v]:
            newCost = cost[v]+next[1]
            if newCost < cost[next[0]]:
                cost[next[0]] = newCost
                heapq.heappush(hq,(newCost,next[0]))

    return cost[end]

path1 = dijkstra(1,mid1) + dijkstra(mid1,mid2) + dijkstra(mid2,n)
path2 = dijkstra(1,mid2) + dijkstra(mid2,mid1) + dijkstra(mid1,n)
if (path1 != math.inf) or (path2 != math.inf):
    print(min(path1,path2))
else:
    print(-1)