import sys
input = sys.stdin.readline

sys.setrecursionlimit(int(2e4))

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

while True:
    n,m = 0,0
    try:
        n,m = map(int,input().split())
    except:
        break

    graph = [[] for _ in range(2*n+1)]
    for _ in range(m):
        s,e = map(int,input().split())
        graph[-s].append(e)
        graph[-e].append(s)

    scc = find_scc()
    ans = 'yes'
    for i in range(1,2*n+1):
        if scc[i] == scc[-i]:
            ans = 'no'
            break
    if ans == 'no':
        print(ans)
        continue

    found = [0]*(n+1)
    for i in range(-n,n+1):
        if i == 0:
            continue
        if scc[i] <= scc[1]:
            found[abs(i)] += 1

    if any([i == 2 for i in found]):
        print('no')
    else:
        print('yes')
