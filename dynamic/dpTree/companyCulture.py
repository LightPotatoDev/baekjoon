import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
L = list(map(int,input().split()))
for i,x in enumerate(L):
    if x == -1:
        continue
    graph[i+1].append(x)
    graph[x].append(i+1)

dp = [0]*(n+1)
for _ in range(m):
    i,w = map(int,input().split())
    dp[i] += w

visited = [0]*(n+1)

def treeDp(cur):
    if visited[cur] == 1:
        return
    visited[cur] = 1

    for node in graph[cur]:
        if not visited[node]:
            dp[node] += dp[cur]
            treeDp(node)

treeDp(1)
print(*dp[1:])
