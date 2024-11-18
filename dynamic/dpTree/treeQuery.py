import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n,r,q = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
nodeNum = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def set_nodes(n):
    visited[n] = 1
    node = 1
    for i in graph[n]:
        if visited[i] == 0:
            node += set_nodes(i)
    nodeNum[n] = node
    return node

set_nodes(r)

for _ in range(q):
    u = int(input())
    print(nodeNum[u])