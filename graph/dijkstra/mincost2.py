import sys
import math
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

start,end = map(int,input().split())

def dijkstra():
    hq = [(0,start)] #가중치, 위치
    cost = [math.inf] * (n+1)
    cost[start] = 0
    trace = [[start] for _ in range(n+1)]

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for next in graph[v]:
            newCost = cost[v]+next[1]
            if newCost < cost[next[0]]:
                cost[next[0]] = newCost
                heapq.heappush(hq,(newCost,next[0]))
                trace[next[0]] = trace[v] + [next[0]]

    return (cost,trace)

c,t = dijkstra()
print(c[end])
print(len(t[end]))
print(*t[end])

#n의 최댓값이 1000이라서 역추적 안써도 통과되는거 같음