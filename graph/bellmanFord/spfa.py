import sys
input = sys.stdin.readline
from collections import deque

INF = int(1e10)

def spfa(start):

    cost = [INF] * (n+1)
    cost[start] = 0
    dq = deque([start])
    dq_exist = [False]*(n+1)
    dq_exist[start] = True
    cycle = [0]*(n+1)

    while dq:
        u = dq.popleft()
        dq_exist[u] = False

        for w,v in graph[u]:
            if cost[v] > cost[u]+w:
                cost[v] = cost[u]+w
                if dq_exist[v] == False:
                    cycle[v] += 1
                    if cycle[v] >= n:
                        return -1
                    dq_exist[v] = True
                    dq.append(v)

    return cost
