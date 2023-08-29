import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
items = [0] + list(map(int,input().split()))
graph = [[int(5e6)]*(n+1) for _ in range(n+1)]

for _ in range(r):
    s,e,w = map(int,input().split())
    graph[s][e] = w
    graph[e][s] = w

for i in range(1,n+1):
    graph[i][i] = 0

def floyd():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

floyd()

maxFarm = 0
for zone in graph[1:]:
    farm = 0
    for i,x in enumerate(zone):
        if x <= m:
            farm += items[i]
    maxFarm = max(maxFarm, farm)

print(maxFarm)