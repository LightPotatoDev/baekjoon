import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = [(0,start)]
    cost = [int(3e6)] * (n+1)
    cost[start] = 0
    trace = [[start] for _ in range(n+1)]

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for nw,nv in graph[v]:
            newCost = cost[v]+nw
            if newCost < cost[nv]:
                cost[nv] = newCost
                heapq.heappush(hq,(newCost,nv))
                trace[nv] = trace[v] + [nv]

    return trace

T = int(input())
for _ in range(T):

    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))

    dest = [int(input()) for _ in range(t)]
    paths = dijkstra(s)
    print(paths)
    ans = []
    for i in dest:
        pathSet = set(paths[i])
        if g in pathSet and h in pathSet:
            gInd = paths[i].index(g)
            hInd = paths[i].index(h)
            if abs(gInd-hInd) == 1:
                ans.append(i)
    ans.sort()
    print(*ans)