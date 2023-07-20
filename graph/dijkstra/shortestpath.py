import sys
import math
import heapq
input = sys.stdin.readline

vertex,edge = map(int,input().split())

graph = [[] for _ in range(vertex+1)]
start = int(input())

for _ in range(edge):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

def dijkstra():
    hq = [(0,start)] #가중치, 위치
    cost = [math.inf] * (vertex+1)
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

    return cost

for i in dijkstra()[1:]:
    if i != math.inf:
        print(i)
    else:
        print("INF")