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

T = int(input())
for _ in range(T):
    n,m,k = map(int,input().split())
    graph = [[] for _ in range(2*(n+m)+1)]
    for _ in range(k):
        a,b,c,d = map(int,input().split())
        r1,r2,c1,c2 = 0,0,0,0
        if a != c and b != d:
            if b < d:
                r1 = a
                r2 = c
            else:
                r1 = -a
                r2 = -c

            if a < c:
                c1 = (b+n)
                c2 = (d+n)
            else:
                c1 = -(b+n)
                c2 = -(d+n)

            graph[-r1].append(r2)
            graph[-r2].append(r1)
            graph[-c2].append(r2)
            graph[-r2].append(c2)
            graph[-r1].append(c1)
            graph[-c1].append(r1)
            graph[-c2].append(c1)
            graph[-c1].append(c2)
        elif a == c and b != d:
            if b < d:
                r1 = a
            else:
                r1 = -a
            graph[-r1].append(r1)
        elif a != c and b == d:
            if a < c:
                c1 = b+n
            else:
                c1 = -(b+n)
            graph[-c1].append(c1)

    scc = find_scc()
    ans = 'Yes'
    for i in range(1,2*(n+m)+1):
        if scc[i] == scc[-i]:
            ans = 'No'
            break

    print(ans)
