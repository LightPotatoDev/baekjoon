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
            if dp[p]+w > dp[v]:
                dp[v] = dp[p]+w
                trace[v] = p
            if indegree[v] == 0:
                dq.append(v)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+2)]
indegree = [0] * (n+2)
trace = [0] * (n+2)
dp = [0] * (n+2)
dp[n] = 1
for _ in range(m):
    x,y,k = map(int,input().split())
    if y == 1:
        y = n+1
    graph[x].append((k,y))
    indegree[y] += 1

topoSort()
print(dp[n+1])
back = n+1
L = [1]
while back != 0:
    back = trace[back]
    if back != 0:
        L.append(back)
print(*L[::-1])
