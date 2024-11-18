import sys
input = sys.stdin.readline

sys.setrecursionlimit(int(1e4))

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)

for i in graph:
    i.sort()

node_id = 0
def scc():
    stk = []
    res = []
    order = [-1]*(n+1)
    parent = [-1]*(n+1)
    finished = [0]*(n+1)

    def dfs(u):
        global node_id
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
            L = []
            while stk:
                p = stk.pop()
                L.append(p)
                finished[p] = 1
                if p == u:
                    break
            res.append(L)

        return parent[u]

    for i in range(1,n+1):
        if order[i] == -1:
            dfs(i)

    return res

ans = scc()
for group in ans:
    group.sort()
ans.sort()
print(len(ans))
for group in ans:
    print(*group, end=' ')
    print(-1)
