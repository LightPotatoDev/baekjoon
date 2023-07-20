import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(1,n+1):
    line = list(map(int,input().split()))
    for j,x in enumerate(line):
        if x == 1:
            graph[i].append(j+1)

def bfs(graph, checked, start):
    dq = deque([start])

    while dq:
        v = dq.popleft()
        for edge in graph[v]:
            if checked[edge] == 0:
                dq.append(edge)
                checked[edge] = 1
    return checked

for i in range(1,n+1):
    checked = [0] * (n+1)
    checked = bfs(graph,checked,i)
    print(*checked[1:])