import sys
input = sys.stdin.readline
from collections import deque

INF = int(1e10)

def network_flow(source, sink):
    total_flow = 0

    while True:
        parent = [-1]*(nc)
        stk = [source]

        while stk and parent[sink] == -1:
            u = stk.pop()
            for v in adj[u]:
                if capacity[u][v] - flow[u][v] > 0 and parent[v] == -1:
                    parent[v] = u
                    stk.append(v)

        if parent[sink] == -1:
            break

        amount = int(1e10)
        v = sink
        while v != source:
            amount = min(amount, capacity[parent[v]][v]-flow[parent[v]][v])
            v = parent[v]

        v = sink
        while v != source:
            flow[parent[v]][v] += amount
            flow[v][parent[v]] -= amount
            v = parent[v]
        total_flow += amount

    return total_flow

def get_adj(i,j):
    v = []
    if i-1 >= 0:
        v.append((i-1)*m+j+1)
    if i+1 < n:
        v.append((i+1)*m+j+1)
    if j-1 >= 0:
        v.append(i*m+j)
    if j+1 < m:
        v.append(i*m+j+2)

    return v

def add_edge(u,v,c):
    capacity[u][v] = c
    adj[u].append(v)
    adj[v].append(u)

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    nc = n*m+2
    adj = [[] for _ in range(nc)]
    flow = [[0]*nc for _ in range(nc)]
    capacity = [[0]*nc for _ in range(nc)]
    grid = [list(map(int,input().split())) for _ in range(n)]
    SRC = 0
    SINK = n*m+1
    white_sum = 0
    black_sum = 0

    for i in range(n):
        for j in range(m):
            u = i*m+j+1
            if (i+j)%2 == 0:
                vv = get_adj(i,j)
                for v in vv:
                    add_edge(u,v,1000)
                add_edge(SRC,u,grid[i][j])
                white_sum += grid[i][j]
            else:
                add_edge(u,SINK,grid[i][j])
                black_sum += grid[i][j]

    f = network_flow(SRC,SINK)
    print(f + (white_sum-f) + (black_sum-f))