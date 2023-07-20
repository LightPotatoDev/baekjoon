import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(checked, target):
    dq = deque([1])

    while dq:
        v = dq.popleft()
        for edge in graph[v]:
            if edge == target:
                return v
            if checked[edge] == 0:
                dq.append(edge)
                checked[edge] = 1

for i in range(2,n+1):
    checked = [0] * (n+1)
    checked[1] = 1
    print(bfs(checked,i))