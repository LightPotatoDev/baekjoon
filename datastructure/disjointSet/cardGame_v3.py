import sys
input = sys.stdin.readline
from bisect import bisect_right

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.maxCard = data

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
            root1.maxCard = max(root1.maxCard,root2.maxCard)
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.maxCard = max(root1.maxCard,root2.maxCard)

    def __repr__(self):
        return str(self.data)


def nearUnion(node,i):
    if 0<=i<=m-1 and N[i] != 0:
        node.union(N[i])

n,m,k = map(int,input().split())
Cards = list(map(int,input().split()))
Cards.sort()
Opponent = list(map(int,input().split()))
N = [0]*m

for i in Opponent:
    ind = bisect_right(Cards,i)
    if N[ind] != 0:
        ind = bisect_right(Cards,N[ind].find().maxCard)

    N[ind] = Node(Cards[ind])
    print(Cards[ind])
    nearUnion(N[ind],ind-1)
    nearUnion(N[ind],ind+1)