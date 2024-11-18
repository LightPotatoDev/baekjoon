import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
p1,p2 = map(int,input().split())
m = int(input())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    checked = [0] * (n+1)
    dq = deque([start])

    while dq:
        v = dq.popleft()
        for edge in graph[v]:
            if checked[edge] == 0:
                dq.append(edge)
                checked[edge] = checked[v] + 1

    return checked[p2]

ans = bfs(p1)
if ans == 0:
    print(-1)
else:
    print(ans)