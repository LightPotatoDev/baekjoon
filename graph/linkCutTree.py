import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.size = 1

    def find(self):
        root = self
        while root != root.next:
            root = root.next
        return root

    def union(self, node):
        root1 = self.find()
        root2 = node.find()
        if root1 == root2:
            return

        if root1.rank >= root2.rank:
            root2.next = root1
            root1.size += root2.size
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.size += root1.size

    def __repr__(self):
        return str(self.data)

def dfs(u,par,i):
    global cycle
    if cycle == True:
        return

    visited[u] = (i,par)
    for i,v in graph[u]:
        if v == par:
            continue
        if visited[v][0] == -1:
            dfs(v, u,i)
        elif visited[v][0] != -1 and finished[v] == 0:
            cycle = True
            return

    finished[u] = 1


T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(m)]
    nodes = [Node(i) for i in range(n+1)]
    graph = [[] for _ in range(n+1)]
    visited = [(-1,0)]*(n+1)
    finished = [0]*(n+1)
    cycle = False
    root = 0
    root2 = 0
    ans = []

    for i,x in enumerate(edges):
        a,b = x
        graph[a].append((i+1,b))
        graph[b].append((i+1,a))
        if nodes[a].find() == nodes[b].find():
            root,root2 = a,b
            ans.append(i+1)
            break
        nodes[a].union(nodes[b])

    dfs(root, -1,0)
    if cycle == False:
        print(-1)
        continue
    u = root2
    while u != -1:
        if visited[u][0] != 0:
            ans.append(visited[u][0])
        u = visited[u][1]
    ans.sort()
    print(*ans)