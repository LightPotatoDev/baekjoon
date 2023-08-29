import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.cantUse = True
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
            root1.maxCard = max(root1.maxCard, root2.maxCard)
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.maxCard = max(root1.maxCard, root2.maxCard)

    def __repr__(self):
        return str(self.leastGate)


def nearUnion(node,i):
    if 1<=i<=int(4e6)+1 and N[i].cantUse == True:
        node.union(N[i])

n,m,k = map(int,input().split())
N = [0]+[Node(i) for i in range(1,int(4e6)+1)]
Cards = list(map(int,input().split()))

for i in Cards:
    N[i].cantUse = False

for i in range(1,int(4e6)):
    if N[i].cantUse and N[i+1].cantUse:
        N[i].union(N[i+1])

Opponent = list(map(int,input().split()))
for i in Opponent:
    num = i+1
    card = N[num]
    if card.cantUse == True:
        num = card.find().maxCard+1
        card = N[num]

    card.cantUse = True
    print(num)
    nearUnion(card,num-1)
    nearUnion(card,num+1)
