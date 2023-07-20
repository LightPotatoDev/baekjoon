import sys
import math
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[math.inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s][e] = w
    graph[e][s] = w

for i in range(1,n+1):
    graph[i][i] = 0

start,end = map(int,input().split())

def dijkstra():
    cost = graph[start][:]
    hq = [(cost[start],start)]

    while hq:
        v = heapq.heappop(hq)
        for i in range(1,n+1):
            cost[i] = min(cost[i], cost[v]+graph[v][i])
            heapq.heappush(hq,(cost[i],i))
        print(hq)

    return cost

print(dijkstra()[end])