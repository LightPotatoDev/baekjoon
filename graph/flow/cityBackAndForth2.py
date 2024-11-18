import sys
input = sys.stdin.readline
from collections import deque

n,p = map(int,input().split())
capacity = [[0]*(2*n+1) for _ in range(2*n+1)]
flow = [[0]*(2*n+1) for _ in range(2*n+1)]

for _ in range(p):
    a,b = map(int,input().split())
    if a > b:
        a,b = b,a
    a_in, a_out = (a-2)*2+1, (a-2)*2+2
    b_in, b_out = (b-2)*2+1, (b-2)*2+2
    if a <= 2:
        capacity[a][b_in] = 1
        capacity[b_in][b_out] = 1
        capacity[b_out][a] = 1
    else:
        capacity[a_in][a_out] = 1
        capacity[a_out][b_in] = 1
        capacity[b_in][b_out] = 1
        capacity[b_out][a_in] = 1

def network_flow(source, sink):
    total_flow = 0

    while True:
        parent = [-1]*(2*n+1)
        dq = deque([source])

        while dq and parent[sink] == -1:
            u = dq.popleft()
            for v in range(2*n+1):
                if capacity[u][v] - flow[u][v] > 0 and parent[v] == -1:
                    parent[v] = u
                    dq.append(v)

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

print(network_flow(1,2))