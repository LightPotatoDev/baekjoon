import sys
input = sys.stdin.readline

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

T = int(input())
for _ in range(T):
    f = int(input())
    people = dict()

    for _ in range(f):
        p1,p2 = input().rstrip().split()

        p1Node = people.get(p1)
        p2Node = people.get(p2)
        if not p1Node:
            p1Node = Node(p1)
            people[p1] = p1Node
        if not p2Node:
            p2Node = Node(p2)
            people[p2] = p2Node

        p1Node.union(p2Node)
        print(p1Node.find().size)



