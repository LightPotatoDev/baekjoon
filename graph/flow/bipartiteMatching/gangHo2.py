import sys
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [[0]*(2*n+1) for _ in range(2*n+1)]
match = [0]*(m+1)
graph = [[] for _ in range(2*n+1)]

for i in range(n):
    work = list(map(int,input().split()))[1:]
    graph[2*i+1] = work
    graph[2*i+2] = work

def dfs(nth_match,u):
    if visited[nth_match][u]:
        return 0
    visited[nth_match][u] = 1
    for v in graph[u]:
        if not match[v] or dfs(nth_match,match[v]):
            match[v] = u
            return 1
    return 0

def bimatch():
    match_count = 0
    for i in range(1,2*n+1):
        match_count += dfs(i,i)

    return match_count

print(bimatch())