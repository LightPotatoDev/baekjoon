import sys
input = sys.stdin.readline
from collections import deque

PAR_SIZE = 17

n = int(input())
graph = [[] for _ in range(n+1)]
depth = [0]*(n+1)
tree = [0]*(n+1)
par = [[0]*(n+1) for _ in range(PAR_SIZE)]

for _ in range(n-1):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))

def make_tree(root):
    visited = [0]*(n+1)
    depth[root] = 1
    dq = deque([root])
    while dq:
        p = dq.popleft()
        visited[p] = 1
        for w,v in graph[p]:
            if visited[v] == 0:
                dq.append(v)
            else:
                tree[p] = (w,v)
                depth[p] = depth[v]+1
    tree[root] = (0,root)

make_tree(1)

par[0] = tree
for i in range(1,PAR_SIZE):
    for j in range(1,n+1):
        w,v = par[i-1][j]
        nw,nv = par[i-1][v]
        par[i][j] = (w+nw,nv)

def lca(a,b):
    if (depth[a]>depth[b]):
        a,b = b,a
    depth_diff = depth[b]-depth[a]

    cost = 0

    for i in range(PAR_SIZE):
        if ((depth_diff >> i) & 1) == 1:
            cost += par[i][b][0]
            b = par[i][b][1]
    if a == b:
        return cost

    for i in range(PAR_SIZE-1,-1,-1):
        if par[i][a][1] != par[i][b][1]:
            cost += par[i][a][0] + par[i][b][0]
            a = par[i][a][1]
            b = par[i][b][1]
    return cost + par[0][a][0] + par[0][b][0]

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))