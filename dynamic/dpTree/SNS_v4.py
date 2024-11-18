import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [0]*(n+1)
dp = [[1,0] for _ in range(n+1)]

def treeDp(cur):
    if visited[cur] == 1:
        return dp[cur]
    visited[cur] = 1

    for node in graph[cur]:
        if not visited[node]:
            dp[cur][0] += min(treeDp(node))
            dp[cur][1] += treeDp(node)[0]

    return dp[cur]

treeDp(1)
print(min(dp[1]))