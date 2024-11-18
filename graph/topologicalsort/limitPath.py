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
                trace[v] = [p]
            elif dp[p]+w == dp[v]:
                trace[v].append(p)

            if indegree[v] == 0:
                dq.append(v)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
dp = [0] * (n+1)
trace = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,k = map(int,input().split())
    graph[x].append((k,y))
    indegree[y] += 1
s,e = map(int,input().split())

topoSort()
print(dp[e])
back = deque([e])
roads = set()
while back:
    p = back.popleft()
    for v in trace[p]:
        if (p,v) not in roads:
            roads.add((p,v))
            back.append(v)

print(len(roads))