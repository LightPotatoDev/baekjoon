import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, checked, start):
    dq = deque([start])

    while dq:
        v = dq.popleft()
        for edge in graph[v]:
            if checked[edge] == 0:
                dq.append(edge)
                checked[edge] = 1
    return checked

checked = [0] * (n+1)
checked[0] = 1
connections = 0

for i in range(1,n+1):
    if checked[i] == 0:
        checked = bfs(graph,checked,i)
        connections += 1

print(connections)