import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)

topo = deque()
visited = [0] * (n+1)

def dfs(start):
    stack = [start]
    visitlist = []

    while stack:
        print(stack, visitlist)
        p = stack.pop()

        if visited[p] == 0:
            visited[p] = 1
            visitlist.append(p)
            stack.extend(graph[p])
        else:
            topo.appendleft(visitlist.pop())
    topo.extendleft(visitlist[::-1])


for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i)

print(*topo)
