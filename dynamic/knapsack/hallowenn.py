import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.candy = 0
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
            root1.candy += root2.candy
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.size += root1.size
            root2.candy += root1.candy

    def __repr__(self):
        return str(self.find().candy) + " " + str(self.find().size)

n,m,k = map(int,input().split())
N = [0]+[Node(i) for i in range(1,n+1)]
Candy = list(map(int,input().split()))
for i,x in enumerate(Candy):
    N[i+1].candy = x
for _ in range(m):
    a,b = map(int,input().split())
    N[a].union(N[b])

S = set()
for node in N[1:]:
    S.add((node.find().data,node.find().candy,node.find().size))
S = [0]+list(S)
dp = [[0]*k for _ in range(len(S))]

for i in range(1,len(S)):
    root,candy,size = S[i]
    for j in range(1,k):
        if j-size < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-size]+candy)

print(dp[len(S)-1][k-1])

for row in dp:
    print(row)

print(S)