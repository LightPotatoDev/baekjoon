import sys
input = sys.stdin.readline
from collections import deque

n,p = map(int,input().split())
capacity = [[0]*(n+1) for _ in range(n+1)]
flow = [[0]*(n+1) for _ in range(n+1)]

for _ in range(p):
    a,b = map(int,input().split())
    capacity[a][b] = 1

def network_flow(source, sink):
    total_flow = 0

    while True:
        parent = [-1]*(n+1)
        dq = deque([source])

        while dq and parent[sink] == -1:
            u = dq.popleft()
            for v in range(n+1):
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