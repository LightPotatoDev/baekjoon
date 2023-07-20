import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
real = list(map(int,input().split()[1:]))

graph = [set() for _ in range(n+1)]
parties = []
for _ in range(m):
    people = set(map(int,input().split()[1:]))
    parties.append(people)
    for i in people:
        graph[i] = graph[i] | people

def bfs(start):
    dq = deque([start])

    while dq:
        p = dq.popleft()
        if visited[p] == 0:
            visited[p] = 1
            dq.extend(graph[p])

visited = [0] * (n+1)
for i in real:
    if visited[i] == 0:
        bfs(i)

cnt = 0
for people in parties:
    cnt += 1
    for i in people:
        if visited[i] == 1:
            cnt -= 1
            break
print(cnt)