import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
depth = [0] * (n+1)
depth[1] = 1
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    dq = deque([1])

    while dq:
        v = dq.popleft()
        for edge in graph[v]:
            if depth[edge] == 0:
                dq.append(edge)
                depth[edge] = depth[v] + 1

bfs()

for i in range(2,n+1):
    for j in graph[i]:
        if depth[i] == depth[j] + 1:
            print(j)
            break

""" by mize159
parent = [0] * (n + 1)
q = [1]
vis = [False] * (n + 1)
while q:
    t = q.pop()
    for next in graph[t]:
        if not vis[next]:
            vis[next] = True
            parent[next] = t
            q.append(next)

print('\n'.join(map(str, parent[2:])))
"""