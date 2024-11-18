import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

nodeId = 0
def find_scc():
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

while True:
    inp = list(map(int,input().split()))
    if inp[0] == 0:
        break

    n,m = inp
    graph = [[] for _ in range(n+1)]
    graphR = [[] for _ in range(n+1)]
    connect = list(map(int,input().split()))
    for i in range(m):
        s,e = connect[i*2], connect[i*2+1]
        graph[s].append(e)
        graphR[e].append(s)

    scc = find_scc()
    sink = []
    for group in scc:
        is_sink = True
        for v in group:
            if is_sink == False:
                break
            for nv in graph[v]:
                if nv not in group:
                    is_sink = False
                    break
        if is_sink:
            sink.extend(group)
    sink.sort()
    print(*sink)