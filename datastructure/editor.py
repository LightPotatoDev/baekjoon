import sys
input = sys.stdin.readline

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        self.length = 0
        if nodes != None:
            self.length = len(nodes)
            node = Node(data=nodes.pop(0))
            self.head = node
            for i in nodes:
                node.next = Node(data=i)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node != None:
            nodes.append(node.data)
            node = node.next
        return "".join(nodes)

    def appendleft(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            prev = self.head
            while prev.next:
                prev = prev.next
            prev.next = node
        self.length += 1

    def insert(self, pos, data):
        if pos == 0:
            self.appendleft(data)
        elif pos == self.length:
            self.append(data)
        else:
            node = Node(data)
            prev = self.head
            for _ in range(pos-1):
                prev = prev.next
            node.next = prev.next
            prev.next = node
            self.length += 1

    def popleft(self):
        if self.head == None:
            return
        self.head = self.head.next
        self.length -= 1

    def pop(self, pos):
        if self.length == 0:
            return
        if pos <= 1:
            self.popleft()
        else:
            prev = self.head
            for _ in range(pos-2):
                prev = prev.next
            if pos == self.length:
                prev.next = None
            else:
                prev.next = prev.next.next
            self.length -= 1

s = input().rstrip()
m = int(input())
L = LinkedList(list(s))
p = len(s)

for _ in range(m):
    cmd = input().rstrip().split()
    if cmd[0] == "L" and p > 0:
        p -= 1
    elif cmd[0] == "D" and p < L.length:
        p += 1
    elif cmd[0] == "B" and p > 0:
        L.pop(p)
        p -= 1
    elif cmd[0] == "P":
        L.insert(p,cmd[1])
        p += 1

print(L)
