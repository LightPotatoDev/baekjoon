import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    L = list(map(int,input().split()))
    s = L[0]
    for i in range(len(L)//2-1):
        graph[s].append((L[2*i+1], L[2*i+2]))

visited = [0]*(n+1)
dp = [0]*(n+1)

ans = 0

def treeDp(cur):
    global ans
    if visited[cur] == 1:
        return dp[cur]
    visited[cur] = 1

    for node,weight in graph[cur]:
        if not visited[node]:
            val = treeDp(node)+weight
            ans = max(ans,dp[cur]+val)
            dp[cur] = max(dp[cur],val)

    return dp[cur]

treeDp(1)
print(ans)
