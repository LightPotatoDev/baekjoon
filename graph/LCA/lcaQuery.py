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
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def make_tree(root):
    visited = [0]*(n+1)
    depth[root] = 1
    dq = deque([root])
    while dq:
        p = dq.popleft()
        visited[p] = 1
        for v in graph[p]:
            if visited[v] == 0:
                dq.append(v)
            else:
                tree[p] = v
                depth[p] = depth[v]+1
    tree[root] = root

make_tree(1)

par[0] = tree
for i in range(1,PAR_SIZE):
    for j in range(1,n+1):
        par[i][j] = par[i-1][par[i-1][j]]

def lca(a,b):
    if (depth[a]>depth[b]):
        a,b = b,a
    depth_diff = depth[b]-depth[a]

    for i in range(PAR_SIZE):
        if ((depth_diff >> i) & 1) == 1:
            b = par[i][b]
    if a == b:
        return a

    for i in range(PAR_SIZE-1,-1,-1):
        if par[i][a] != par[i][b]:
            a = par[i][a]
            b = par[i][b]
    return par[0][a]

m = int(input())
for _ in range(m):
    r,a,b = map(int,input().split())
    lcas = [lca(a,b),lca(a,r),lca(b,r)]
    print(min(lcas, key = lambda x:-depth[x]))