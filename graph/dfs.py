from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in graph:
    i.sort()

#DFS
def dfs():
    visited = [0] * (n+1)
    dq = deque([v])
    order = 1

    while dq:
        if visited[dq[0]] == 0:
            visited[dq[0]] = order
            order += 1

        deadend = True
        for i in graph[dq[0]]:
            if visited[i] == 0:
                dq.appendleft(i)
                deadend = False
                break

        if deadend == True:
            dq.popleft()

    return visited


for i in dfs()[1:]:
    print(i)
