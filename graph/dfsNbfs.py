from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())
relations = []
for _ in range(m):
    x,y = map(int,input().split())
    relations.append([x,y])
    relations.append([y,x])

#DFS
checked = [0] * (n+1)
dq = deque()
dq.append(v)
L = []
while dq:
    thisvisit = []
    node = dq.pop()

    if checked[node] == 1:
        continue
    else:
        checked[node] = 1
        L.append(node)

    for j in relations:
        if j[0] == node and checked[j[1]] == 0:
            thisvisit.append(j[1])
    for i in sorted(thisvisit,reverse=True):
        dq.append(i)
print(' '.join(map(str,L)))


#BFS
checked = [0] * (n+1)
dq = deque()
dq.append(v)
checked[v] = 1
L = []
while dq:
    thisvisit = []
    node = dq.popleft()
    L.append(node)
    for j in relations:
        if j[0] == node and checked[j[1]] == 0:
            checked[j[1]] = 1
            thisvisit.append(j[1])
    for i in sorted(thisvisit):
        dq.append(i)

print(' '.join(map(str,L)))

"""by codestudy25

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

    #relation 대신 1:[2,3,4] ,2:[3,5] 와 같이 vertex:[vertexes] 관계 사용

for i in graph:
  i.sort()

visited_dfs = [False] * (N+1)
def dfs(graph, visited_dfs, v):
    visited_dfs[v] = True
    print(v, end = ' ')

    for edge in graph[v]:
        if not visited_dfs[edge]:
            dfs(graph, visited_dfs, edge)

visited_bfs = [False] *(N+1)

from collections import deque

def bfs(graph, visited_bfs, start):
    queue = deque([start])
    visited_bfs[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for edge in graph[v]:
            if not visited_bfs[edge]:
                queue.append(edge)
                visited_bfs[edge] = True
"""