import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))

n = int(input())
graph = [[] for _ in range(n+1)]
weight = [0]+list(map(int,input().split()))
for _ in range(n-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [0]*(n+1)
dp = [[0]*2 for _ in range(n+1)]

def treeDp(cur):
    if visited[cur] == 1:
        return dp[cur]
    visited[cur] = 1

    dp[cur][1] = weight[cur]

    for node in graph[cur]:
        if not visited[node]:
            dp[cur][0] += max(treeDp(node)[0], treeDp(node)[1])
            dp[cur][1] += treeDp(node)[0]

    return dp[cur]

treeDp(1)

visited = [0]*(n+1)
ans = []
def traceBack(cur,side):
    if visited[cur] == 1:
        return
    visited[cur] = 1

    if side == 1:
        ans.append(cur)

    for node in graph[cur]:
        if not visited[node]:
            if side == 1:
                traceBack(node,0)
            else:
                traceBack(node,dp[node][0] < dp[node][1])


traceBack(1,dp[1][0] < dp[1][1])
print(max(dp[1]))
ans.sort()
print(*ans)