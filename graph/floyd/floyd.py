import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[math.inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s][e] = min(graph[s][e], w)

for i in range(1,n+1):
    graph[i][i] = 0

def floyd():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

floyd()

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == math.inf:
            graph[i][j] = 0

for row in graph[1:]:
    print(*row[1:])

"""
frmt = "{:>5}"*(n)
for row in graph[1:]:
    print(frmt.format(*row[1:]))
print('')
"""