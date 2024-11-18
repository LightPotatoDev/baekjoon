import sys
input = sys.stdin.readline

sys.setrecursionlimit(int(2e4))

node_id = 0
scc_id = 0
def find_scc():
    stk = []
    res = [-1]*(2*(n+m)+1)
    order = [-1]*(2*(n+m)+1)
    parent = [-1]*(2*(n+m)+1)
    finished = [0]*(2*(n+m)+1)

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

    for i in range(1,2*(n+m)+1):
        if order[i] == -1:
            dfs(i)

    return res

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
graph = [[] for _ in range(2*(n+m)+1)]
for i in range(n):
    for j in range(m):
        a = i+1
        b = n+j+1
        if grid[i][j] == '*':
            graph[a].append(-b)
            graph[b].append(-a)
            graph[-a].append(b)
            graph[-b].append(a)
        elif grid[i][j] == '#':
            graph[-a].append(-b)
            graph[b].append(a)
            graph[a].append(b)
            graph[-b].append(-a)

scc = find_scc()
for i in range(1,2*(n+m)+1):
    if scc[i] == scc[-i]:
        print(0)
        exit()

print(1)
