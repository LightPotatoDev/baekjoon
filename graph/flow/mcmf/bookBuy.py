import sys
input = sys.stdin.readline
from collections import deque

INF = int(1e10)
SRC = 0
SINK = 1

n,m = map(int,input().split())
nc = n+m+2 #node_count
adj = [[] for _ in range(nc)]
cap = [[0]*(nc) for _ in range(nc)]
dist = [[0]*(nc) for _ in range(nc)]
flow = [[0]*(nc) for _ in range(nc)]

A = list(map(int,input().split()))
for i in range(n):
    cap[SRC][i+2] = A[i]
    adj[SRC].append(i+2)
    adj[i+2].append(SRC)

B = list(map(int,input().split()))
for i in range(m):
    cap[i+n+2][SINK] = B[i]
    adj[SINK].append(i+n+2)
    adj[i+n+2].append(SINK)

for i in range(m):
    C = list(map(int,input().split()))
    for j in range(n):
        u = j+2
        v = i+n+2
        d = C[j]
        adj[u].append(v)
        adj[v].append(u)
        cap[u][v] = 100
        dist[u][v] += d
        dist[v][u] -= d

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

mc,mf = mcmf()
print(mc)