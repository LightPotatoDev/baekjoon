import sys
input = sys.stdin.readline
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1

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
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2

    def __repr__(self):
        return str(self.data)

n = int(input())
N = [0]+[Node(i) for i in range(1,n+1)]
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    N[a].union(N[b])
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [0] * (n+1)
    nxt = deque([start])
    dq = deque()
    steps = 0

    while nxt:
        dq = nxt.copy()
        nxt = deque()
        while dq:
            p = dq.popleft()

            if visited[p] == 0:
                visited[p] = 1
                nxt.extend(graph[p])
        steps += 1

    return steps

Groups = dict()
for node in N[1:]:
    root = node.find()
    if root in Groups:
        Groups[root].append(node.data)
    else:
        Groups[root] = [node.data]

print(len(Groups))
Admins = []
for group in Groups.values():
    admin = 0
    minConnect = 999
    for i in group:
        connect = bfs(i)
        if connect < minConnect:
            admin = i
            minConnect = connect
    Admins.append(admin)

Admins.sort()
for i in Admins:
    print(i)