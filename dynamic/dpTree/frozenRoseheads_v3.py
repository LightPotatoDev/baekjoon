import sys
input = sys.stdin.readline
from collections import deque

class Node:
    def __init__(self):
        self.parent = 0
        self.water = 0

while True:
    n,c = 0,0
    try:
        n,c = map(int,input().split())
    except:
        break

    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(n-1):
        u,v,w = map(int,input().split())
        graph[u].append((w,v))
        graph[v].append((w,u))

    dqTraverse = deque([c])
    dqSolve = deque()
    nodes = [Node() for _ in range(n+1)]
    while dqTraverse:
        p = dqTraverse.popleft()
        visited[p] = 1
        for w,v in graph[p]:
            if visited[v] == 1:
                nodes[p].parent = v
            else:
                dqTraverse.append(v)