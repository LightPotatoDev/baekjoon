from itertools import combinations
import heapq
import sys
input = sys.stdin.readline

n,t = map(int,input().split())
graph = [[] for _ in range(n+1)]

City = [[i+1] + list(map(int,input().split())) for i in range(n)]
comb = combinations(City,2)
for c1,c2 in comb:
    n1,s1,x1,y1 = c1
    n2,s2,x2,y2 = c2
    dist = abs(x1-x2) + abs(y1-y2)
    tele = t
    if s1 != 1 or s2 != 1:
        tele = int(3e3)
    graph[n1].append([n2,min(tele,dist)])
    graph[n2].append([n1,min(tele,dist)])

def dijkstra(start,end):
    hq = [(0,start)]
    cost = [int(3e3)] * (n+1)
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

    return cost[end]

m = int(input())
for _ in range(m):
    s,e = map(int,input().split())
    print(dijkstra(s,e))