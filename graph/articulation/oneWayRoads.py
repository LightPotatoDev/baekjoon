import sys
input = sys.stdin.readline

time = 1
def find_bridge():

    def dfs_bridge(u,par):
        global time
        visited[u] = time
        low[u] = time
        time += 1

        for v in graph[u]:
            if visited[v] == 0:
                visit_order.append((u,v))
                dfs_bridge(v,u)
                low[u] = min(low[u], low[v])
                if low[v] > visited[u]:
                    bridges.append((u,v))
            elif v != par:
                low[u] = min(low[u], visited[v])
            elif v == par:
                visit_order.append((u,v))

    visited = [0]*(n+1)
    low = [0]*(n+1)

    bridges = []
    visit_order = []

    for i in range(1,n+1):
        if visited[i] == 0:
            dfs_bridge(i,-1)

    return (bridges, visit_order)

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    bridges, visit_order = find_bridge()
    if len(bridges) > 0:
        print('NO')
    else:
        print('YES')
        for a,b in visit_order:
            print(a,b)