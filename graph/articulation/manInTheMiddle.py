import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(3e5))

time = 1
def find_ap():

    def dfs_ap(u,par):
        global time
        children = 0
        visited[u] = time
        low[u] = time
        time += 1

        for v in graph[u]:
            if visited[v] == 0:
                children += 1
                dfs_ap(v,u)
                low[u] = min(low[u], low[v])
                if par != -1 and low[v] >= visited[u]:
                    is_ap[u] = True
            elif v != par:
                low[u] = min(low[u], visited[v]) #found back edge

        if par == -1 and children >= 2:
            is_ap[u] = True

    visited = [0]*(n+1)
    low = [0]*(n+1)

    is_ap = [False]*(n+1)

    for i in range(1,n+1):
        if visited[i] == 0:
            dfs_ap(i,-1)

    return is_ap

t = int(input())
for _ in range(t):

    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    ans = find_ap()
    if sum(ans) > 0:
        print('YES')
    else:
        print('NO')