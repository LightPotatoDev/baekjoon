import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(start, visitlist, depth):
    global noTeams

    visited[start] = depth

    for i in visitlist:
        if visited[i] == 0:
            dfs(i, graph[i], depth+1)
        elif finished[i] == 0:
            noTeams -= (depth - visited[i] + 1)

    finished[start] = 1

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    L = list(map(int,input().split()))
    noTeams = n
    for i,x in enumerate(L):
        graph[i+1].append(x)

    visited = [0] * (n+1)
    finished = [0] * (n+1)

    for i in range(1,n+1):
        if visited[i] == 0:
            dfs(i, graph[i], 1)

    print(noTeams)