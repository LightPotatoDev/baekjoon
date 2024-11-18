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

    def insert(self,string):
        node = self.head
        for s in string:
            if s not in node.child:
                node.child[s] = Node(s)
            node = node.child[s]
        node.isEnd = True

    def search(self,string):
        node = self.head
        for s in string:
            if s not in node.child:
                return False
            node = node.child[s]
        return node.isEnd

    def out(self,node,depth):
        D = list(node.child)
        D.sort()
        for i in D:
            print("--"*depth + i)
            self.out(node.child[i],depth+1)

    def __repr__(self):
        return str(self.head.child)


n = int(input())
tr = Trie()
for _ in range(n):
    L = list(input().rstrip().split())[1:]
    tr.insert(L)

tr.out(tr.head,0)