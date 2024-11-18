import sys
input = sys.stdin.readline
from collections import deque

def treeDp(cur):
    visited[cur] = 1

    for w,v in graph[cur]:
        if not visited[v]:
            dp[cur] += min(treeDp(v), w)

    return dp[cur]

while True:
    n,c = 0,0
    try:
        n,c = map(int,input().split())
    except:
        break

    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(n-1):
        u,v,w = map(int,input().split())
        graph[u].append((w,v))
        graph[v].append((w,u))

    dp = [0]*(n+1)
    for i in range(1,n+1):
        if len(graph[i]) == 1 and i != c:
            dp[i] = graph[i][0][0]

    treeDp(c)
    print(dp[c])