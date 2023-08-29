import math
import sys
input = sys.stdin.readline

def bellmanFord(start):

    cost = [math.inf] * n
    cost[start] = 0

    for i in range(m):
        updated = False
        for s in range(n):
            for e,w in graph[s]:
                if cost[e] > cost[s]+w:
                    cost[e] = cost[s]+w
                    updated = True
        if not updated:
            break
        if i == m-1 and updated == True:
            return "Gee"

    return cost[end]

n,start,end,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append([e,w])
money = list(map(int,input().split()))

for v in range(n):
    for i,x in enumerate(graph[v]):
        graph[v][i][1] -= money[graph[v][i][0]]

print(bellmanFord(start))