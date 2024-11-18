import sys
input = sys.stdin.readline
from collections import deque

INF = int(1e10)

def mcmf():
    mc = 0
    mf = 0
    while True:
        parent = [-1]*nc
        cost = [INF]*nc
        cost[SRC] = 0

        dq = deque([SRC])
        dq_exist = [False]*nc
        dq_exist[SRC] = True

        while dq:
            u = dq.popleft()
            dq_exist[u] = False

            for v in adj[u]:
                if cap[u][v] - flow[u][v] > 0 and cost[v] > cost[u]+dist[u][v]:
                    cost[v] = cost[u]+dist[u][v]
                    parent[v] = u
                    if dq_exist[v] == False:
                        dq_exist[v] = True
                        dq.append(v)

        if parent[SINK] == -1:
            break

        amount = INF
        v = SINK
        while v != SRC:
            amount = min(amount, cap[parent[v]][v]-flow[parent[v]][v])
            v = parent[v]

        v = SINK
        while v != SRC:
            mc += amount * dist[parent[v]][v]
            flow[parent[v]][v] += amount
            flow[v][parent[v]] -= amount
            v = parent[v]
        mf += amount

    return (mc,mf)

def add_edge(u,v,c,w):
    adj[u].append(v)
    adj[v].append(u)
    dist[u][v] = w
    dist[v][u] = -w
    cap[u][v] = c

while True:
    n,m = 0,0
    try:
        n,m = map(int,input().split())
    except:
        break

    SRC = 0
    SINK = n*2-1
    nc = n*2+1 #node_count
    adj = [[] for _ in range(nc)]
    cap = [[0]*(nc) for _ in range(nc)]
    dist = [[0]*(nc) for _ in range(nc)]
    flow = [[0]*(nc) for _ in range(nc)]

    for i in range(n):
        u_in = i*2+1
        u_out = i*2+2
        add_edge(u_in,u_out,1,0)

    for _ in range(m):
        u,v,w = map(int,input().split())
        u_out = 2*u
        v_in = 2*v-1
        add_edge(u_out,v_in,1,w)

    add_edge(SRC,1,2,0)
    cap[1][2] = 2

    print(mcmf()[0])