import sys
input = sys.stdin.readline

class Edge:
    def __init__(self,v,capacity,flow):
        self.v = v
        self.capacity = capacity
        self.flow = flow
        self.rev_idx = 0

    def __repr__(self):
        return f'v:{self.v}/flow:{self.flow}'

def add_edge(u,v,cap):
    graph[u].append(Edge(v,cap,0))
    graph[v].append(Edge(u,0,0))
    graph[u][-1].rev_idx = len(graph[v]) - 1
    graph[v][-1].rev_idx = len(graph[u]) - 1

def search_edge(u,v):
    for e in graph[u]:
        if e.v == v:
            return e
    return -1

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
node_count = (n*m)*2
graph = [[] for _ in range(node_count)]
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

        u_in = (i*m+j)*2
        u_out = (i*m+j)*2+1
        add_edge(u_in,u_out,1)

        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] != '#':
                v_in = (ny*m+nx)*2
                add_edge(u_out,v_in,1)
                if grid[i][j] == 'K' and grid[ny][nx] == 'H':
                    print(-1)
                    exit()

def network_flow(source, sink):
    total_flow = 0

    while True:
        parent = [-1]*(node_count)
        stk = [source]

        while stk and parent[sink] == -1:
            u = stk.pop()
            for edge in graph[u]:
                if edge.capacity - edge.flow > 0 and parent[edge.v] == -1:
                    parent[edge.v] = u
                    stk.append(edge.v)

        if parent[sink] == -1:
            break

        amount = int(1e10)
        v = sink
        while v != source:
            par = search_edge(parent[v],v)
            amount = min(amount, par.capacity - par.flow)
            v = parent[v]

        v = sink
        while v != source:
            par = search_edge(parent[v],v)
            par.flow += amount
            rev = graph[par.v][par.rev_idx]
            rev.flow -= amount
            v = parent[v]
        total_flow += amount

    return total_flow

print(network_flow(s,e))