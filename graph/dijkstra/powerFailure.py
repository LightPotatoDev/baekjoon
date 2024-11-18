import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,end):
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

    return cost[end]

n,w = map(int,input().split())
m = float(input())
pos = [[0,0] for _ in range(n+1)]
connected = [[0]*(n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    pos[i][0],pos[i][1] = map(int,input().split())

for i in range(w):
    a,b = map(int,input().split())
    connected[a][b] = 1
    connected[b][a] = 1

for i in range(1,n+1):
    for j in range(i+1,n+1):
        x1,y1 = pos[i]
        x2,y2 = pos[j]
        dist = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
        #if dist > m:
        #    continue

        if connected[i][j] == 1:
            graph[i].append((0,j))
            graph[j].append((0,i))
        else:
            graph[i].append((dist,j))
            graph[j].append((dist,i))

print(int(dijkstra(1,n)*1000))