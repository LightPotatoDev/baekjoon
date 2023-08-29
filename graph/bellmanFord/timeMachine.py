import sys
input = sys.stdin.readline

inf = int(1e8)

def bellmanFord(start):

    cost = [inf] * (n+1)
    cost[start] = 0

    for i in range(m):
        updated = False
        for s in range(1,n+1):
            for e,w in graph[s]:
                if (cost[s] + w != inf) and (cost[e] > cost[s]+w):
                    cost[e] = cost[s]+w
                    updated = True
        if not updated:
            break
        if i == m-1 and updated == True:
            return [-1]

    return cost[2:]

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

for i in bellmanFord(1):
    if i == inf:
        print(-1)
    else:
        print(i)