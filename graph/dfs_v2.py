import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in graph:
    i.sort()

#DFS
def dfs():
    visited = [0] * (n+1)
    stack = [v]
    order = 1

    while stack:
        p = stack.pop()
        if visited[p] == 0:
            visited[p] = order
            order += 1
            stack.extend(graph[p])

    return visited


for i in dfs()[1:]:
    print(i)
