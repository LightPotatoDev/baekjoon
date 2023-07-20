import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)

topo = deque()
visited = [0] * (n+1)

def dfs(start, visitlist):
    visited[start] = 1

    for i in visitlist:
        if visited[i] == 0:
            dfs(i, graph[i])

    topo.appendleft(start)

for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i, graph[i])

print(*topo)
