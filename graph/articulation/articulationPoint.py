import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))

def cut_vertex():
    visited = [0]*(n+1)
    parent = [0]*(n+1)
    is_cut_vertex = [0]*(n+1)
    order = 1

    def dfs(v,is_root):
        visited[v] = order
        parent[v] = order
        order += 1

        for nv in graph[v]:
            if visited[nv] == 0:
                parent[v] = min(parent[v], dfs(nv,False))
            elif finished[nv] == 0:
                parent[v] = min(parent[v], visited[nv])

        finished[v] = 1
        return parent[v]

    for i in range(1,n+1):
        if visited[i] == 0:
            dfs(i,True)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(cut_vertex())