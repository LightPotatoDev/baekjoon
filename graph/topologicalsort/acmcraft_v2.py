import sys
input = sys.stdin.readline

T = int(input())

def dfs(start, visitlist, time):
    global maxtime
    visited[start] = 1

    for i in visitlist:
        if visited[i] == 0:
            dfs(i, graph[i], time+times[i])

    maxtime = max(maxtime, time)
    visited[start] = 0

for _ in range(T):
    n,k = map(int,input().split())
    times = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        s,e = map(int,input().split())
        graph[e].append(s)
    w = int(input())
    maxtime = 0
    visited = [0] * (n+1)

    dfs(w, graph[w], times[w])
    print(maxtime)
