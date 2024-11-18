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

def compute_kth_node(dist_a,dist_b,a,b,lca,k):
    #dist_a - number of nodes visited from a to lca (inclusive)
    if k > dist_a:
        return compute_kth_node(dist_b,dist_a,b,a,lca,dist_a+dist_b-k)

    k -= 1
    for i in range(PAR_SIZE):
        if ((k >> i) & 1) == 1:
            a = par[i][a][1]
    return a

def compute_lca(a,b,q,k):
    sa,sb = a,b
    depth_diff = abs(depth[b]-depth[a])

    cost = 0
    dist_a = 1
    dist_b = 1

    for i in range(PAR_SIZE):
        if ((depth_diff >> i) & 1) == 1:
            if depth[a] > depth[b]:
                cost += par[i][a][0]
                dist_a += 1<<i
                a = par[i][a][1]
            elif depth[a] < depth[b]:
                cost += par[i][b][0]
                dist_b += 1<<i
                b = par[i][b][1]
    if a == b and q == 1:
        return cost
    elif a == b and q == 2:
        return compute_kth_node(dist_a,dist_b,sa,sb,b,k)

    for i in range(PAR_SIZE-1,-1,-1):
        if par[i][a][1] != par[i][b][1]:
            cost += par[i][a][0] + par[i][b][0]
            dist_a += 1<<i
            dist_b += 1<<i
            a = par[i][a][1]
            b = par[i][b][1]

    if q == 1:
        return cost + par[0][a][0] + par[0][b][0]
    elif q == 2:
        return compute_kth_node(dist_a+1,dist_b+1,sa,sb,par[0][a][1],k)

m = int(input())
for _ in range(m):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        a,b = cmd[1:]
        print(compute_lca(a,b,1,0))
    elif cmd[0] == 2:
        a,b,k = cmd[1:]
        print(compute_lca(a,b,2,k))