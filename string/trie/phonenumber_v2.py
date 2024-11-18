import sys
input = sys.stdin.readline

class Node:
    def __init__(self,key):
        self.key = key
        self.isEnd = False
        self.child = {}

    def __repr__(self):
        print(str(self.key))

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

    def searchPrefix(self,string):
        node = self.head
        for s in string:
            if node.isEnd == True:
                return True
            node = node.child[s]
        return False


T = int(input())
for _ in range(T):
    n = int(input())
    tr = Trie()
    ans = "YES"
    S = [input().rstrip() for _ in range(n)]

    for s in S:
        tr.insert(s)

    for s in S:
        if tr.searchPrefix(s) == True:
            ans = "NO"
            break

    print(ans)