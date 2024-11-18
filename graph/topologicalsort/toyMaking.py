import sys
input = sys.stdin.readline
from collections import deque

def topoSort():
    dq = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        p = dq.popleft()
        for w,v in graph[p]:
            indegree[v] -= 1
            dp[v] += dp[p] * w
            if indegree[v] == 0:
                dq.append(v)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
outdegree = [0] * (n+1)
dp = [0] * (n+1)
dp[n] = 1
for _ in range(m):
    x,y,k = map(int,input().split())
    graph[x].append((k,y))
    indegree[y] += 1
    outdegree[x] += 1

topoSort()
for i in range(1,n+1):
    if outdegree[i] == 0:
        print(i,dp[i])
