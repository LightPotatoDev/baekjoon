import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))

n = int(input())
graph = [[] for _ in range(n+1)]
ppl = [0]+list(map(int,input().split()))
for _ in range(n-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [0]*(n+1)
dp = [[0]*3 for _ in range(n+1)]

def treeDp(cur):
    if visited[cur] == 1:
        return dp[cur]
    visited[cur] = 1

    dp[cur][2] = ppl[cur]

    for node in graph[cur]:
        if not visited[node]:
            dp[cur][0] += max(treeDp(node)[0], treeDp(node)[2])
            dp[cur][1] += treeDp(node)[0]
            dp[cur][2] += max(treeDp(node)[0], treeDp(node)[1])

    return dp[cur]

treeDp(1)

print(max(dp[1][0], dp[1][2]))