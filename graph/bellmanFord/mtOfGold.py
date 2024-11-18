import sys
input = sys.stdin.readline
from collections import deque

INF = int(1e10)

def spfa(start):

    cost = [INF] * n
    cost[start] = 0
    dq = deque([start])
    dq_exist = [False]*n
    dq_exist[start] = True
    cycle = [0]*n

    while dq:
        u = dq.popleft()
        dq_exist[u] = False

        for w,v in graph[u]:
            if cost[v] > cost[u]+w:
                cost[v] = cost[u]+w
                if dq_exist[v] == False:
                    cycle[v] += 1
                    if cycle[v] > 2*n:
                        return cycle
                    dq_exist[v] = True
                    dq.append(v)

    return cycle

def bfs(start):
    visited = [False]*n
    dq = deque([start])
    while dq:
        u = dq.popleft()
        visited[u] = True
        for w,v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                dq.append(v)

    return visited[0]


t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((w,v))

    cycle = spfa(0)
    ans = False
    for u in range(n):
        if cycle[u] >= n and bfs(u) == True:
            ans = True
            break
    if ans == False:
        print(f'Case #{tc}: not possible')
    else:
        print(f'Case #{tc}: possible')
