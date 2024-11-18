import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,end):
    hq = [(0,start)]
    cost = [int(3e6)] * (n+1)
    cost[start] = 0

    while hq:
        w,v = heapq.heappop(hq)
        if cost[v] < w:
            continue
        for nw,nv in graph[v]:
            newCost = cost[v]+nw
            if newCost < cost[nv]:
                cost[nv] = newCost
                heapq.heappush(hq,(newCost,nv))

    return cost[end]

T = int(input())
for _ in range(T):

    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    costGH = 0

    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))
        if ((a==g and b==h) or (b==g and a==h)):
            costGH = d

    dest = [int(input()) for _ in range(t)]

    ans = []
    for e in dest:
        costMin = dijkstra(s,e)
        costSG = dijkstra(s,g)
        costSH = dijkstra(s,h)
        costGE = dijkstra(g,e)
        costHE = dijkstra(h,e)
        if ((costSG + costGH + costHE == costMin) or (costSH + costGH + costGE == costMin)):
            ans.append(e)
    ans.sort()
    print(*ans)