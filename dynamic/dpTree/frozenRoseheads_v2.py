import sys
input = sys.stdin.readline
from collections import deque

while True:
    n,c = 0,0
    try:
        n,c = map(int,input().split())
    except:
        break

    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    dp = [0] * (n+1)
    for _ in range(n-1):
        u,v,w = map(int,input().split())
        graph[u].append((w,v))
        graph[v].append((w,u))

    dq = deque([c])
    outDegree = [0] * (n+1)

    while dq:
        p = dq.popleft()
        visited[p] = 1

        if len(graph[p]) == 1 and p != c:
            dp[p] = graph[p][0][0]
        for w,v in graph[p]:
            if visited[v] == 0:
                dq.append(v)
                outDegree[p] += 1

    dq = deque()
    visited = [0] * (n+1)
    for i in range(1,n+1):
        if outDegree[i] == 0:
            dq.append(i)

    while dq:
        p = dq.popleft()

