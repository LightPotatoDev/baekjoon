import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n = int(input())
graph = [set() for _ in range(n+1)]
child = [set() for _ in range(n+1)]
parent = [-1] * (n+1)
visited = [0]*(n+1)
for _ in range(n-1):
    s,e = map(int,input().split())
    graph[s].add(e)
    graph[e].add(s)

def make_tree(root):
    visited[root] = 1
    for i in graph[root]:
        if visited[i] == 0:
            child[root].add(i)
            make_tree(i)

make_tree(1)

for i in range(1,n+1):
    P = graph[i]-child[i]
    if P:
        parent[i] = P.pop()

Nodes = []
for i,x in enumerate(child[1:]):
    if not x:
        Nodes.append(i+1)

visited = [0]*(n+1)
ans = 0
while Nodes:
    nxt = []
    for i in Nodes:
        prnt = parent[i]
        if prnt == -1:
            continue
        if prnt == 1 and visited[i] == 1:
            continue

        if visited[prnt] == 0:
            visited[prnt] = 1
            ans += 1
            prntprnt = parent[prnt]
            if prntprnt != -1:
                nxt.append(prntprnt)
    Nodes = nxt[:]

print(ans)
