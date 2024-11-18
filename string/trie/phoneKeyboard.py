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

    def search(self,string):
        cnt = 1
        node = self.head
        for i,s in enumerate(string):
            if (len(node.child) != 1 or node.isEnd == True) and i != 0:
                cnt += 1
            node = node.child[s]
        return cnt


while True:
    n = 0
    try:
        n = int(input())
    except:
        break

    tr = Trie()
    S = [input().rstrip() for _ in range(n)]

    for s in S:
        tr.insert(s)

    cnt = 0
    for s in S:
        cnt += tr.search(s)

    print("{:.2f}".format(round(cnt/n,2)))