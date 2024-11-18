import sys
input = sys.stdin.readline
T = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.group = {data}
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
            root1.group = root1.group | root2.group
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.group = root1.group | root2.group

    def __repr__(self):
        return str(self.group)

def merge(a,b):
    if L[a]+L[b] <= w:
        graph[a].add(b)
        graph[b].add(a)

def deleteGraph(a):
    for i in graph[a]:
        graph[i].remove(a)
    graph[a] = set()

def matching(L):
    S = set(L)
    pair = 0

    while True:
        has1Degree = False
        delV = []
        print(S)

        for i in S:
            if len(graph[i]) == 0:
                delV.append(i)
            if len(graph[i]) == 1:
                pair += 1
                has1Degree = True
                a = graph[i].pop()
                graph[i].add(a)

                delV.append(i)
                delV.append(a)
                deleteGraph(a)
                break

        for i in delV:
            S.remove(i)

        if has1Degree == False:
            break

    print(pair)
    pair += len(S) // 2
    return pair

for _ in range(T):
    n,w = map(int,input().split())
    L = list(map(int,input().split())) + list(map(int,input().split()))

    graph = [set() for _ in range(2*n)]
    for i in range(n):
        merge(i,(i+1)%n)
        merge(i,i+n)
        merge(i+n,(i+1)%n+n)

    #print(graph)

    N = [Node(i) for i in range(2*n)]
    cycle = False
    for i in range(2*n):
        for v in graph[i]:
            N[i].union(N[v])

    S = set()
    for i in N:
        S.add(tuple(i.find().group))

    ans = 2*n
    for i in S:
        if len(i) >= 2:
            ans -= matching(i)
    print(ans)