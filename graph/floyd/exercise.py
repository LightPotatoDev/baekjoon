import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[int(5e6)]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s][e] = w

for i in range(1,n+1):
    graph[i][i] = 0

def floyd():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

floyd()

d = int(5e6)
for i in range(1,n+1):
    for j in range(1,n+1):
        if i != j:
            d = min(d, graph[i][j] + graph[j][i])

if d < int(5e6):
    print(d)
else:
    print(-1)