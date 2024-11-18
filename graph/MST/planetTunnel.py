import sys
input = sys.stdin.readline

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
Planets = [[i]+list(map(int,input().split())) for i in range(n)] #[num,x,y,z]
graph = []
for i in range(1,4):
    Planets.sort(key=lambda x:x[i])
    for j in range(n-1):
        n1, p1 = Planets[j][0], Planets[j][i]
        n2, p2 = Planets[j+1][0], Planets[j+1][i]
        graph.append([n1,n2,p2-p1])
graph.sort(key=lambda x:x[2])

N = [Node(i) for i in range(n)]
ans = 0
for a,b,c in graph:
    if N[a].find() != N[b].find():
        N[a].union(N[b])
        ans += c

print(ans)