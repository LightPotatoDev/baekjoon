import sys
input = sys.stdin.readline

def dfs(nth_match,u):
    if visited[nth_match][u]:
        return 0
    visited[nth_match][u] = 1
    for v in graph[u]:
        if match[v] == -1 or dfs(nth_match,match[v]):
            match[v] = u
            return 1
    return 0

def bimatch():
    match_count = 0
    for i in range(n):
        match_count += dfs(i,i)

    return match_count

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    visited = [[0]*n for _ in range(n)]
    match = [-1]*n
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
    print(bimatch())