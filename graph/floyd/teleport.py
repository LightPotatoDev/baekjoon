from itertools import combinations
import sys
input = sys.stdin.readline

n,t = map(int,input().split())
graph = [[int(1e8)]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0

City = [[i+1] + list(map(int,input().split())) for i in range(n)]
comb = combinations(City,2)
for c1,c2 in comb:
    n1,s1,x1,y1 = c1
    n2,s2,x2,y2 = c2
    graph[n1][n2] = abs(x1-x2) + abs(y1-y2)
    graph[n2][n1] = abs(x1-x2) + abs(y1-y2)
    if s1 == 1 and s2 == 1:
        graph[n1][n2] = min(t,graph[n1][n2])
        graph[n2][n1] = min(t,graph[n2][n1])

def floyd():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]

floyd()
m = int(input())
for _ in range(m):
    s,e = map(int,input().split())
    print(graph[s][e])