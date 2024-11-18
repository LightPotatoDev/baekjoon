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

def hori_stamp(i,j):
    return i*50+j+1

def verti_stamp(i,j):
    return 2500+i*50+j+1

def get_match(i,j):
    v = []
    if j-1 >= 0:
        v.append(hori_stamp(i,j-1))
    if j+1 < m:
        v.append(hori_stamp(i,j))
    if i-1 >= 0:
        v.append(verti_stamp(i-1,j))
    if i+1 < n:
        v.append(verti_stamp(i,j))
    return v

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())

    #0 - SRC
    #1   ~2500 - 가로 스탬프
    #2501~5000 - 세로 스탬프
    #5001~7500 - 블록
    #7501 - SINK

    SRC = 0
    SINK = 7501
    nc = 7502
    grid = [list(map(int,input().split())) for _ in range(n)]
    adj = [[] for _ in range(nc)]
    cap = [[0]*(nc) for _ in range(nc)]
    dist = [[0]*(nc) for _ in range(nc)]
    flow = [[0]*(nc) for _ in range(nc)]

    for i in range(n):
        for j in range(m):
            add_edge(SRC,i*m+j+2,grid[i][j],0)

    for i in range(n):
        for j in range(m):
            u = i*m+j+2
            vv = get_match(i,j)
            for v in vv:
                add_edge(u,v,1000,1)

    for i in range(n):
        for j in range(m-1):
            u = n*m+2 + i*(m-1)+j
            add_edge(u,SINK,1000,0)

    for i in range(n-1):
        for j in range(m):
            u = n*m+2 + (m-1)*n + i*m+j
            add_edge(u,SINK,1000,0)

    print(mcmf())