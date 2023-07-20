import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def dfs(start, visitlist):
    visited[start] = 1

    for i in visitlist:
        if visited[i] == 0:
            dfs(i, graphR[i])

    topo.append(start)

for _ in range(T):
    n,k = map(int,input().split())
    times = [0] + list(map(int,input().split()))
    graphR = [[] for _ in range(n+1)] #Reversed
    for _ in range(k):
        s,e = map(int,input().split())
        graphR[e].append(s)
    w = int(input())
    visited = [0] * (n+1)
    topo = deque()

    dfs(w, graphR[w])

    timespent = [0] * (n+1)
    for x in topo:
        timespent[x] += times[x]
        timespent[x] += max([timespent[i] for i in graphR[x]], default = 0)

    print(timespent[w])