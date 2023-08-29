import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)

def bfs():
    visited = [0] * (n+1)
    dq = deque([(x,1)])

    while dq:
        p,d = dq.popleft()

        if visited[p] == 0:
            visited[p] = d
            dq.extend(zip(graph[p],[d+1]*len(graph[p])))

    return visited

nothing = True
for i,x in enumerate(bfs()[1:]):
    if x == k+1:
        print(i+1)
        nothing = False

if nothing:
    print(-1)
