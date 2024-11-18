import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((w,e))

trace = [[] for _ in range(n)]

def bfs(start):
    visited = [0]*n
    visited[start] = 1
    nodes = deque([start])

    while nodes:
        p = nodes.popleft()
        for w,e in graph[p]:
            if visited[e] == 0:
                nodes.append(e)
                visited[e] = visited[p]+1
            if visited[e] == visited[p]+1:
                trace[e].append(p)

print(trace)

ans = int(1e12)
def backtrace(nxt,cost):
    if not nxt:
        ans = min(ans,cost)
    for i in nxt:
        backtrace(trace[i],)