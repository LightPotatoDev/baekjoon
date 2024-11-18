def sieve(n):
    is_prime = [0,1] * (n//2+1)

    for i in range(3,n+1,2):
        if is_prime[i]:
            for j in range(i*3,n+1,i*2):
                is_prime[j] = 0

    is_prime[1] = 0
    is_prime[2] = 1
    return is_prime

is_prime = sieve(2000)
n = int(input())
L = list(map(int,input().split()))
visited = [[0]*(n+1) for _ in range(n+1)]
match = [0]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]

for i,x in enumerate(L):
    for j,y in enumerate(L):
        if is_prime[x+y] and x != y:
            graph[i+1][j+1] = 1

def dfs(nth_match,u):
    if visited[nth_match][u]:
        return 0
    visited[nth_match][u] = 1
    for v in range(n+1):
        if graph[u][v] == 1 and (not match[v] or dfs(nth_match,match[v])):
            match[v] = u
            return 1
    return 0

def bimatch():
    match_count = 0
    for i in range(1,n+1):
        match_count += dfs(i,i)

    return match_count

def remove_edges(v):
    rm = []
    for u in range(n+1):
        if graph[u][v] == 1:
            rm.append((u,v))
    for u,v in rm:
        graph[u][v] = 0
    return rm

def restore_edges(rm):
    for u,v in rm:
        graph[u][v] = 1

first_num_match = [i for i in range(n+1) if graph[1][i] == 1]
graph[1] = [0]*(n+1)
ans = []
for i in first_num_match:
    rm = remove_edges(i)
    if bimatch() == n-1:
        ans.append(L[i-1])
        for g in graph:
            print(g)
        print(rm)
    restore_edges(rm)

if ans:
    print(*ans)
else:
    print(-1)