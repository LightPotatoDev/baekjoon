import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.weight = 0
        self.known = False
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

def experiment(a,b,w):
    n1 = N[a]
    n2 = N[b]

    if n1.known == False and n2.known == False:
        n2.weight += w
    elif n1.known == True and n2.known == False:
        n2.weight += n1.weight+w
    elif n1.known == False and n2.known == True:
        n1.weight += n2.weight-w
    elif n1.find() != n2.find():
        increment = n1.weight-n2.weight+w
        for node in n2.find().child:
            node.weight += increment

    n1.known = True
    n2.known = True
    n1.union(n2)

def answer(a,b):
    if N[a].find() == N[b].find():
        print(N[b].weight - N[a].weight)
    else:
        print("UNKNOWN")

while True:
    n,m = map(int,input().split())
    N = [0]+[Node(i) for i in range(1,n+1)]
    if n == 0:
        break

    for _ in range(m):
        inp = input().rstrip().split()

        if inp[0] == "!":
            a,b,w = map(int,inp[1:])
            experiment(a,b,w)
        elif inp[0] == "?":
            a,b = map(int,inp[1:])
            answer(a,b)

