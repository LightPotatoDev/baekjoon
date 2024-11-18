import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
L = list(map(int,input().split()))
for i,x in enumerate(L):
    if x == -1:
        continue
    graph[i].append([x,0])
    graph[x].append([i,0])

visited = [0]*n
depth = [0]*n
def treeDepth(cur):
    if visited[cur] == 1:
        return graph[cur][1]
    visited[cur] = 1

    for node,depth in graph[cur]:
        if visited[node] == 0:
            graph[cur][1] += treeDepth(node)

    return graph[cur][1]

print(d)
treeDepth(0)

graph[i].sort(key = lambda x:-x[1])

print(graph)

dp = [0]*n
visited = [0]*n
def treeDp(cur):
    if visited[cur] == 1:
        return
    visited[cur] = 1

    time = 1
    for node,a in graph[cur]:
        if visited[node] == 0:
            dp[node] = dp[cur] + time
            time += 1
            print(dp,cur)
            treeDp(node)

treeDp(0)
print(*dp)
