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
    for i in range(n*2):
        match_count += dfs(i,i)

    return match_count

n = int(input())
visited = [[0]*(n*2) for _ in range(n*2)]
match = [-1]*n
graph = [[] for _ in range(n*2)]
sharks = [tuple(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        a,b,c = sharks[i]
        d,e,f = sharks[j]
        if a >= d and b >= e and c >= f:
            if a != d or b != e or c != f:
                graph[i*2].append(j)
                graph[i*2+1].append(j)
            elif i > j:
                graph[i*2].append(j)
                graph[i*2+1].append(j)

print(n - bimatch())