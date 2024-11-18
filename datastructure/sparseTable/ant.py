import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
energy = [int(input()) for _ in range(n)]
graph = [[] for _ in range(n)]
tree = [0 for _ in range(n)]
ST = [[0]*(n) for _ in range(16)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

def makeTree(root):
    visited = [0]*(n)
    dq = deque([root])
    while dq:
        p = dq.popleft()
        visited[p] = 1
        for v,c in graph[p]:
            if visited[v] == 0:
                dq.append(v)
            else:
                tree[p] = (v,c)

makeTree(0)
tree[0] = (0,0)
ST[0] = tree
for i in range(1,16):
    for j in range(n):
        v,c = ST[i-1][j]
        ST[i][j] = (ST[i-1][v][0],c + ST[i-1][v][1])

for j,e in enumerate(energy):
    for i in range(15,-1,-1):
        if ST[i][j][1] <= e:
            e -= ST[i][j][1]
            j = ST[i][j][0]
    print(j+1)