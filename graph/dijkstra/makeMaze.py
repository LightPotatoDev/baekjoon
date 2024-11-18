import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,end):
    hq = [(0,start)]
    cost = [int(1e10)] * (nn+1)
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

n = int(input())
L = [list(map(int,list(input().rstrip()))) for _ in range(n)]
graph = [[] for _ in range(n**2+1)]
nn = n ** 2

dy = [-1,0,0,1]
dx = [0,-1,1,0]
for i in range(n):
    for j in range(n):
        for dir in range(4):
            ny = i + dy[dir]
            nx = j + dx[dir]
            if not (0<=ny<n and 0<=nx<n):
                continue

            nodeFrom = i*n+j+1
            nodeTo = ny*n+nx+1
            graph[nodeFrom].append((int(L[ny][nx] == 0),nodeTo))

print(dijkstra(1,nn))

