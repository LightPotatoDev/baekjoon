import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
indoors = '0'+input().rstrip()
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
ans = 0

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dq = deque([start])
    visited[dq[0]] = True
    in_nodes = 0
    while dq:
        u = dq.popleft()
        for v in graph[u]:
            if indoors[v] == '1':
                in_nodes += 1
            elif indoors[v] == '0' and visited[v] == False:
                visited[v] = True
                dq.append(v)

    return (in_nodes-1) * in_nodes

def nearby_check(u):
    res = 0
    for v in graph[u]:
        if indoors[v] == '1':
            res += 1
    return res

for i in range(1,n+1):
    if indoors[i] == '0' and visited[i] == False:
        ans += bfs(i)
    elif indoors[i] == '1':
        ans += nearby_check(i)

print(ans)