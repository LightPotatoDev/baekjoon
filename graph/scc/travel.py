import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

nodeId = 0
def scc():
    sccStk = []
    res = []
    order = [-1]*(n+1)
    parent = [-1]*(n+1)
    finished = [0]*(n+1)

    def dfs(v):
        global nodeId
        nodeId += 1
        order[v] = nodeId
        parent[v] = nodeId
        sccStk.append(v)

        for nv in graph[v]:
            if order[nv] == -1:
                parent[v] = min(parent[v], dfs(nv))
            elif finished[nv] == 0:
                parent[v] = min(parent[v], order[nv])

        if parent[v] == order[v]:
            L = []
            while sccStk:
                p = sccStk.pop()
                L.append(p)
                finished[p] = 1
                if p == v:
                    break
            res.append(L)

        return parent[v]

    for i in range(1,n+1):
        if order[i] == -1:
            dfs(i)

    return res

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
if len(scc()) == 1:
    print("Yes")
else:
    print("No")