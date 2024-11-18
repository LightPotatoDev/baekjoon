import sys
input = sys.stdin.readline
T = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.group = {data}
        self.rank = 1

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
            root1.group = root1.group | root2.group
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.group = root1.group | root2.group

    def __repr__(self):
        return str(self.group)

def merge(a,b):
    if L[a]+L[b] <= w:
        graph[a].add(b)
        graph[b].add(a)

def fillblocks(base,S):
    dp = [[-1]*4 for _ in range(n)]

    dp[0][0] = 0
    if base == 0 and (0 in graph[n]):
        dp[0][3] = 1
    if base == 1:
        dp[0][1] = 1
    if base == 2:
        dp[0][2] = 1

    for i in range(1,n):
        dp[i][0] = max(dp[i-1])
        if (i in graph[i-1]) and (base != 1 or i != n-1):
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + 1
        if (n+i in graph[n+i-1]) and (base != 2 or i != n-1):
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + 1
        if (i in graph[n+i]):
            dp[i][3] = max(dp[i-1]) + 1

    return max(dp[r-1])

def matching(L):
    S = set(L)
    res = max(fillblocks(0,S),res)

    if (0 in graph[n-1]):
        res = max(fillblocks(1,S),res)

    if (n in graph[2*n-1]):
        res = max(fillblocks(2,S),res)

    return res

for _ in range(T):
    n,w = map(int,input().split())
    L = list(map(int,input().split())) + list(map(int,input().split()))

    graph = [set() for _ in range(2*n)]
    for i in range(n):
        merge(i,(i+1)%n)
        merge(i,i+n)
        merge(i+n,(i+1)%n+n)

    N = [Node(i) for i in range(2*n)]
    for i in range(2*n):
        for v in graph[i]:
            N[i].union(N[v])

    S = set()
    for i in N:
        S.add(tuple(i.find().group))

    ans = 2*n
    for i in S:
        if 2 <= len(i) <= 3:
            ans -= 1
        elif len(i) >= 4:
            ans -= matching(i)
    print(ans)