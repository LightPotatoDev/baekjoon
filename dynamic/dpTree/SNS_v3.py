import sys
input = sys.stdin.readline

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
    nodes = [root]
    nxt = []
    while nodes:
        for i in nodes:
            visited[i] = 1
            for c in graph[i]:
                if visited[c] == 0:
                    child[i].add(c)
                    nxt.append(c)
        nodes = nxt[:]
        nxt = []

make_tree(1)

for i in range(1,n+1):
    P = graph[i]-child[i]
    if P:
        parent[i] = P.pop()

Nodes = set()
for i,x in enumerate(child[1:]):
    if not x:
        Nodes.add(i+1)

visited = [0]*(n+1)
ans = 0
while Nodes:
    nxt = set()
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
            if prntprnt != -1 and visited:
                nxt.add(prntprnt)
            parent[prnt] = -1
    Nodes = nxt.copy()

print(ans)
