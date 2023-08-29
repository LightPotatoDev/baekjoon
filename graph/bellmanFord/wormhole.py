import math
import sys
input = sys.stdin.readline

T = int(input())

def bellmanFord(start):

    cost = [math.inf] * (n+2)
    cost[start] = 0

    for i in range(m+worm+1):
        updated = False
        for s in range(1,n+2):
            for e,w in graph[s]:
                if cost[e] > cost[s]+w:
                    cost[e] = cost[s]+w
                    updated = True
        if not updated:
            break
        if i == m+worm and updated == True:
            return "YES"

    return "NO"

for _ in range(T):
    n,m,worm = map(int,input().split())
    graph = [[] for _ in range(n+2)]
    for _ in range(m):
        s,e,w = map(int,input().split())
        graph[s].append((e,w))
        graph[e].append((s,w))
    for _ in range(worm):
        s,e,w = map(int,input().split())
        graph[s].append((e,-w))
    for i in range(1,n+1):
        graph[n+1].append((i,0))

    print(bellmanFord(n+1))