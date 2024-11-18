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
    for i in range(nc):
        match_count += dfs(i,i)

    return match_count

n,k = map(int,input().split())
nc = 2*n
visited = [[0]*nc for _ in range(nc)]
match = [-1]*nc
graph = [[] for _ in range(nc)]
for i in range(k):
    r,c = map(int,input().split())
    graph[r-1].append(n+c-1)

print(bimatch())