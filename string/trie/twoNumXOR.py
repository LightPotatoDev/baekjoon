import sys
input = sys.stdin.readline

class Node:
    def __init__(self,key):
        self.key = key
        self.isEnd = False
        self.child = {}

    def __repr__(self):
        return str(self.key)

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self,num):
        node = self.head
        for i in range(h-1, -1, -1):
            b = ((num >> i) & 1)
            if b not in node.child:
                node.child[b] = Node(b)
            node = node.child[b]
        node.isEnd = True

    def search(self,num):
        node = self.head
        val = 0
        for i in range(h-1, -1, -1):
            b = ((num >> i) & 1)
            if b in node.child:
                val += 1 << i
                node = node.child[b]
            else:
                node = node.child[1-b]

        return val

    def __repr__(self):
        return str(self.head.child)


n = int(input())
N = list(map(int,input().split()))
h = len(bin(max(N)))-2
mask = (1 << h)-1
ans = 0
tr = Trie()

for i in N:
    tr.insert(i)

for i in N:
    target = i ^ mask
    ans = max(ans,tr.search(target))
print(ans)