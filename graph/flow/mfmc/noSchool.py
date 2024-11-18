import sys
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
node_count = (n*m)*2
capacity = [[0]*(node_count) for _ in range(node_count)]
flow = [[0]*(node_count) for _ in range(node_count)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]
s,e = 0,0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            continue
        elif grid[i][j] == 'K':
            s = (i*m+j)*2+1
        elif grid[i][j] == 'H':
            e = (i*m+j)*2
        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] != '#':
                u_in = (i*m+j)*2
                u_out = (i*m+j)*2+1
                v_in = (ny*m+nx)*2
                v_out = (ny*m+nx)*2+1
                capacity[u_in][u_out] = 1
                capacity[u_out][v_in] = 1
                if grid[i][j] == 'K' and grid[ny][nx] == 'H':
                    print(-1)
                    exit()

def network_flow(source, sink):
    total_flow = 0

    while True:
        parent = [-1]*(node_count)
        stk =[source]

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

print(network_flow(s,e))