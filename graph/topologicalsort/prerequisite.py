import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
graphR = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graphR[e].append(s)

visited = [0] * (n+1)

def dfs(start,depth):
    visited[start] = depth

    for i in graph[start]:
        if visited[i] == 0 and all([visited[j]>=1 for j in graphR[i]]):
            dfs(i,depth+1)

for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i,1)

print(*visited[1:])
