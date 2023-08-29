import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    indegree[e] += 1

visited = [0] * (n+1)

def topoSort():
    dq = deque()
    nxt = deque()
    step = 1

    for i in range(1,n+1):
        if indegree[i] == 0:
            dq.append(i)

    while True:
        while dq:
            p = dq.popleft()
            visited[p] = step
            for i in graph[p]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    nxt.append(i)
        if not nxt:
            break

        dq = nxt.copy()
        nxt = deque()
        step += 1

topoSort()
print(*visited[1:])
