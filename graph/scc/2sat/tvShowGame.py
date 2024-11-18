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

n,m = map(int,input().split())
graph = [[] for _ in range(2*n+1)]
for _ in range(m):
    inp = input().rstrip().split()
    for i in range(3):
        if inp[2*i+1] == 'R':
            inp[2*i] = int(inp[2*i])
        elif inp[2*i+1] == 'B':
            inp[2*i] = -int(inp[2*i])

    s1,s2,s3 = inp[0], inp[2], inp[4]
    graph[-s2].append(s1)
    graph[-s1].append(s2)
    graph[-s3].append(s1)
    graph[-s1].append(s3)
    graph[-s2].append(s3)
    graph[-s3].append(s2)

scc = find_scc()
for i in range(1,2*n+1):
    if scc[i] == scc[-i]:
        print(-1)
        exit()

for i in range(1,n+1):
    print('R' if scc[i] < scc[-i] else 'B', end = '')
