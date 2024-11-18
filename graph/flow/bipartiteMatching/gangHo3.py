import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
node_count = n+m+3
capacity = [[0]*(node_count) for _ in range(node_count)]
flow = [[0]*(node_count) for _ in range(node_count)]

for i in range(n):
    work = list(map(int,input().split()))[1:]
    for w in work:
        capacity[i+3][w+n+2] = 1
    capacity[0][i+3] = 1
    capacity[2][i+3] = k
capacity[0][2] = k

for i in range(m):
    capacity[i+n+3][1] = 1

def network_flow(source, sink):
    total_flow = 0

    while True:
        parent = [-1]*(node_count)
        stk = [source]

        while stk and parent[sink] == -1:
            u = stk.pop()
            for v in range(node_count):
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

print(network_flow(0,1))