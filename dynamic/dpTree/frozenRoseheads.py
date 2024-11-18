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
    outDegree = [0]*(n+1)
    dp = [0]*(n+1)
    dq = deque([])
    for _ in range(n-1):
        u,v,w = map(int,input().split())
        graph[u].append((w,v))
        graph[v].append((w,u))

    for i in range(1,n+1):
        outDegree[i] = len(graph[i])
        if outDegree[i] == 1 and i != c:
            dp[i] = graph[i][0][0]
            dq.append(i)
    print(dp)

    while dq:
        p = dq.popleft()
        if p == c:
            continue
        w,v = graph[p][0]
        dp[v] += min(w,dp[p])
        outDegree[v] -= 1
        if outDegree[v] == 0:
            dq.append(v)

    print(dp)
