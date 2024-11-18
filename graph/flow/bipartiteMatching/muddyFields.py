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

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
nc = n*m
visited = [[0]*nc for _ in range(nc)]
match = [-1]*nc
graph = [[] for _ in range(nc)]
connect = [[[-1,-1] for _ in range(m)] for _ in range(n)]

for i in range(n):
    node = 0
    for j in range(m):
        if grid[i][j] == '*':
            if j == 0 or grid[i][j-1] == '.':
                node = i*m+j
            connect[i][j][0] = node

for j in range(m):
    node = 0
    for i in range(n):
        if grid[i][j] == '*':
            if i == 0 or grid[i-1][j] == '.':
                node = i*m+j
            connect[i][j][1] = node

for i in range(n):
    for j in range(m):
        a,b = connect[i][j]
        if a == -1:
            continue
        graph[a].append(b)

print(bimatch())