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
dp = [[[0,[]] for _ in range(2)] for _ in range(n+1)]

def treeDp(cur):
    if visited[cur] == 1:
        return dp[cur]
    visited[cur] = 1

    dp[cur][1][0] = weight[cur]

    for node in graph[cur]:
        if not visited[node]:
            v1 = treeDp(node)[0][0]
            v2,i2 = treeDp(node)[1][0],node
            print(v1,v2)
            if v1 <= v2:
                dp[cur][0][0] += v1
            else:
                dp[cur][0][0] += v2
                dp[cur][0][1].append(i2)

            dp[cur][1][0] += treeDp(node)[0][0]

    return dp[cur]

treeDp(1)

for row in dp:
    print(row)

print(max(dp[1]))