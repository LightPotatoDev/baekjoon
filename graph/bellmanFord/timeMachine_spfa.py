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
                    if cycle[v] > n:
                        return -1
                    dq_exist[v] = True
                    dq.append(v)

    return cost

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u-1].append((w,v-1))

cost = spfa(0)
if cost == -1:
    print(-1)
else:
    for c in cost[1:]:
        print(c) if c != INF else print(-1)