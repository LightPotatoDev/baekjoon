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

    def searchCol(self,string):
        node = self.head
        goodFormat = 0
        for i,s in enumerate(string):
            if s not in node.child:
                break
            node = node.child[s]
            if node.isEnd == True:
                goodFormat += Nick.searchNick(string[i+1:])
        return goodFormat >= 1

    def searchNick(self,string):
        node = self.head
        for s in string:
            if s not in node.child:
                return False
            node = node.child[s]
        return node.isEnd

    def __repr__(self):
        return str(self.head.child)


c,n = map(int,input().split())
Col = Trie()
Nick = Trie()

for _ in range(c):
    Col.insert(input().rstrip())

for _ in range(n):
    Nick.insert(input().rstrip())

q = int(input())
for _ in range(q):
    if Col.searchCol(input().rstrip()):
        print("Yes")
    else:
        print("No")