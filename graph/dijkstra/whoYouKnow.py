import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,end):
    hq = [(0,start)]
    cost = [int(1e10)] * (n+1)
    cost[start] = 0
    trace = [-1]*(n+1)

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for nw,nv in graph[v]:
            newCost = cost[v]+nw
            if newCost < cost[nv]:
                trace[nv] = v
                cost[nv] = newCost
                heapq.heappush(hq,(newCost,nv))

    return trace

T = int(input())
for tc in range(1,T+1):
    m,n = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,l = map(int,input().split())
        graph[a].append((l,b))
        graph[b].append((l,a))

    trace = dijkstra(0,n-1)
    ans = []
    curStep = n-1
    while curStep != -1:
        ans.append(curStep)
        curStep = trace[curStep]

    if 0 in ans:
        print(f"Case #{tc}:",*ans[::-1])
    else:
        print(f"Case #{tc}: -1")