import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

time = 1
def find_bridge():

    def dfs_bridge(u,par):
        global time
        visited[u] = time
        low[u] = time
        time += 1

        for v in graph[u]:
            if visited[v] == 0:
                dfs_bridge(v,u)
                low[u] = min(low[u], low[v])
                if low[v] > visited[u]:
                    if u < v:
                        bridges.append((u,v))
                    else:
                        bridges.append((v,u))
            elif v != par:
                low[u] = min(low[u], visited[v]) #found back edge

    visited = [0]*(n+1)
    low = [0]*(n+1)

    bridges = []

    for i in range(1,n+1):
        if visited[i] == 0:
            dfs_bridge(i,-1)

    return bridges

ans = find_bridge()
ans.sort()
print(len(ans))
for a,b in ans:
    print(a,b)