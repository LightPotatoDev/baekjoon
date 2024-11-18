import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
node_count = n+m+3
capacity = [[0]*(node_count) for _ in range(node_count)]
flow = [[0]*(node_count) for _ in range(node_count)]

books = list(map(int,input().split()))
for i,b in enumerate(books):
    capacity[1][i+3] = b
stores = list(map(int,input().split()))
for i,s in enumerate(stores):
    capacity[i+n+3][2] = s

for i in range(m):
    limit = list(map(int,input().split()))
    for j,l in enumerate(limit):
        capacity[j+3][i+n+3] = l

def network_flow(source, sink):
    total_flow = 0

    while True:
        parent = [-1]*(node_count)
        dq = deque([source])

        while dq and parent[sink] == -1:
            u = dq.popleft()
            for v in range(node_count):
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