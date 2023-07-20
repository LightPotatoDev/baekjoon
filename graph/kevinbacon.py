import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    checked = [0] * (n+1)
    dq = deque([start])

    while dq:
        v = dq.popleft()
        for edge in graph[v]:
            if checked[edge] == 0:
                dq.append(edge)
                checked[edge] = checked[v] + 1
    checked[start] = 0
    return sum(checked)

bacons = []
for i in range(1,n+1):
    bacons.append(bfs(graph,i))

print(min([i+1 for i,x in enumerate(bacons) if x == min(bacons)]))