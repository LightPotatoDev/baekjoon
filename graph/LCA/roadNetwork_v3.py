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
                tree[p] = (w,w,v)
                depth[p] = depth[v]+1
    tree[root] = (0,0,root)

make_tree(1)

def filter_min(a,b):
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return min(a,b)

par[0] = tree
for i in range(1,PAR_SIZE):
    for j in range(1,n+1):
        min_w, max_w,v = par[i-1][j]
        min_nw, max_nw, nv = par[i-1][v]
        par[i][j] = (filter_min(min_w,min_nw),max(max_w,max_nw),nv)

def lca(a,b):
    if (depth[a]>depth[b]):
        a,b = b,a
    depth_diff = depth[b]-depth[a]

    ans_min = int(1e9)
    ans_max = 0

    for i in range(PAR_SIZE):
        if ((depth_diff >> i) & 1) == 1:
            ans_min = min(ans_min, par[i][b][0])
            ans_max = max(ans_max, par[i][b][1])
            b = par[i][b][2]
    if a == b:
        return (ans_min, ans_max)

    for i in range(PAR_SIZE-1,-1,-1):
        if par[i][a][2] != par[i][b][2]:
            ans_min = min(ans_min, par[i][a][0], par[i][b][0])
            ans_max = max(ans_max, par[i][a][1], par[i][b][1])
            a = par[i][a][2]
            b = par[i][b][2]
    return (min(ans_min, par[0][a][0], par[0][b][0]),
            max(ans_max, par[0][a][1], par[0][b][1]))

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    print(*lca(a,b))