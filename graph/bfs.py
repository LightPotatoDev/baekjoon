import sys
input = sys.stdin.readline
from collections import deque

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in graph:
    i.sort(reverse=True)

def bfs():
    visited = [0] * (n+1)
    dq = deque([v])
    order = 1

    while dq:
        p = dq.popleft()

        if visited[p] == 0:
            visited[p] = order
            order += 1
            dq.extend(graph[p])

    return visited


for i in bfs()[1:]:
    print(i)
