import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.parent = self
        self.child = []
        self.par_col = 0
        self.child_col = dict()

    def par_update(self, new_col):
        old = len(self.child_col) - int(par_col in self.child_col)
        new = len(self.child_col) - int(new_col in self.child_col)
        par_col = new_col
        return new - old

    def child_update(self, old_col, new_col):
        old = len(self.child_col)
        self.child_col[old_col] -= 1
        if self.child_col[old_col] == 0:
            del self.child_col[old_col]

        if new_col in self.child_col:
            self.child_col[new_col] += 1
        else:
            self.child_col[new_col] = 1
        new = len(self.child_col)

        return new - old

    def __repr__(self):
        return f'{self.par_col} {self.child_col}'

n,m,q = map(int,input().split())
colors = [0]*n
graph = [[] for _ in range(n+1)]
nodes = [Node() for _ in range(n+1)]
for i in range(1,n+1):
    u,v,w = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    colors[i] = w

#make tree
visited = [False]*(n+1)
def make_tree(par,u):
    visited[u] = True
    for v in graph[u]:
        if visited[v] == False:
            nodes[v].parent = nodes[u]
            nodes[v].par_col =
            make_tree(u,v)