import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    L = list(map(int,input().split()))[1:]
    for i in range(len(L)-1):
        graph[L[i]].append(L[i+1])

topo = deque()
visited = [0] * (n+1)
finished = [0] * (n+1)

def dfs(start, visitlist):
    visited[start] = 1

    for i in visitlist:
        if visited[i] == 0:
            dfs(i, graph[i])
        elif finished[i] == 0:
            print(0)
            exit()

    topo.appendleft(start)
    finished[start] = 1

for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i, graph[i])

for i in topo:
    print(i)
