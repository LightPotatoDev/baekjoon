import sys
input = sys.stdin.readline
from collections import deque

class Node:
    def __init__(self,data,parent,depth,min,max):
        self.data = data
        self.parent = parent
        self.depth = depth
        self.min = min
        self.max = max

    def __repr__(self):
        return f"[{self.data} {self.parent} {self.depth} {self.min} {self.max}]"

    def LCA(self,node):
        a = self
        b = node
        print(a,b)
        if (a.depth > b.depth):
            a,b = b,a
        depthDiff = b.depth - a.depth
        for i in range(17):
            if ((depthDiff >> i) & 1) == 1:
                b = ST[i][b.data].parent
        print(a,b)
        for i in range(16,-1,-1):
            if ST[i][a.data].parent == 1:
                break
            if ST[i][a.data].parent != ST[i][b.data].parent:
                a = ST[i][a.data].parent
                b = ST[i][b.data].parent
        if a == b:
            print(a)
        else:
            print(ST[0][a.data].parent)

n = int(input())
graph = [[] for _ in range(n+1)]
tree = [0]*(n+1)
ST = [[0]*(n+1) for _ in range(17)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def makeTree(root):
    visited = [0]*(n+1)
    tree[root] = Node(root,root,0,0,0)
    dq = deque([root])
    while dq:
        p = dq.popleft()
        visited[p] = 1
        for v,c in graph[p]:
            if visited[v] == 0:
                dq.append(v)
            else:
                tree[p] = Node(p,v,tree[v].depth+1,c,c)

makeTree(1)
ST[0] = tree
for i in range(1,17):
    for j in range(1,n+1):
        node = ST[i-1][ST[i-1][j].parent]
        minVal = min(node.min,ST[i-1][j].min)
        maxVal = max(node.max,ST[i-1][j].max)
        ST[i][j] = Node(j,node.parent,node.depth,minVal,maxVal)
for i in ST:
    print(i)

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    tree[a].LCA(tree[b])