import sys
input = sys.stdin.readline
import heapq

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    indegree[e] += 1

visited = [0] * (n+1)

def topoSort():
    hq = []
    topo = []

    for i in range(1,n+1):
        if indegree[i] == 0:
            heapq.heappush(hq,i)

    while hq:
        p = heapq.heappop(hq)
        visited[p] = 1
        for i in graph[p]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(hq,i)

        topo.append(p)

    return topo

print(*topoSort())
