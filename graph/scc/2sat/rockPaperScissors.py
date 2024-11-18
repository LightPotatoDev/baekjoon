import sys
input = sys.stdin.readline

sys.setrecursionlimit(int(2e5))

node_id = 0
scc_id = 0
def find_scc():
    stk = []
    res = [-1]*(2*n+1)
    order = [-1]*(2*n+1)
    parent = [-1]*(2*n+1)
    finished = [0]*(2*n+1)

    def dfs(u):
        global node_id, scc_id
        node_id += 1
        order[u] = node_id
        parent[u] = node_id
        stk.append(u)

        for v in graph[u]:
            if order[v] == -1:
                parent[u] = min(parent[u], dfs(v))
            elif finished[v] == 0:
                parent[u] = min(parent[u], order[v])

        if parent[u] == order[u]:
            while stk:
                p = stk.pop()
                res[p] = scc_id
                finished[p] = 1
                if p == u:
                    break
            scc_id += 1

        return parent[u]

    for i in range(1,2*n+1):
        if order[i] == -1:
            dfs(i)

    return res

m,n = map(int,input().split())
graph = [[] for _ in range(2*n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[-s].append(e)
    graph[-e].append(s)

scc = find_scc()
ans = '^_^'
for i in range(1,2*n+1):
    if scc[i] == scc[-i]:
        ans = 'OTL'
        break
print(ans)

