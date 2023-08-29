import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)

m = int(input())
for e in range(1,m+1):
    L = list(map(int,input().split()))
    time[e] = L[0]
    indegree[e] = len(L[1:])-1
    for s in L[1:-1]:
        graph[s].append(e)

visited = [0] * (n+1)

def topoSort():
    dq = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        p = dq.popleft()
        visited[p] += time[p]
        for i in graph[p]:
            indegree[i] -= 1
            visited[i] = max(visited[p],visited[i])
            if indegree[i] == 0:
                dq.append(i)

topoSort()
for i in visited[1:]:
    print(i)
