import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.child = [self]

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
            root1.child.extend(root2.child)
        else:
            root1.next = root2
            root2.child.extend(root1.child)

    def __repr__(self):
        return str(self.data)

n,m = map(int,input().split())
roads = [list(map(int,input().split())) for _ in range(m)]
roads.sort(key = lambda x:(x[2],x[3]))
nodes = [0]+[Node(i) for i in range(1,n+1)]

number = []
cost = 0
for u,v,b,c in roads:
    if nodes[u].find() != nodes[v].find():
        nodes[u].union(nodes[v])
        number.append(b)
        cost += c

connected = True
par = nodes[1].find()
for i in range(1,n+1):
    if nodes[i].find() != par:
        connected = False
        break

if connected == False:
    print(-1)
else:
    print(''.join(map(str,number)), end = ' ')
    print(cost)