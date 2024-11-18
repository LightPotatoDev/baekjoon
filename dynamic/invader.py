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
        Mergeable.append([a,b])

def fillblocks(S,r,base):
    dp = [[-1]*4 for _ in range(r)]

    dp[0][0] = 0
    if base == 0 and (0 in S) and (n in S):
        dp[0][3] = 1
    if base == 1:
        dp[0][1] = 1
    if base == 2:
        dp[0][2] = 1

    for i in range(1,r):
        dp[i][0] = max(dp[i-1])
        if (i in S) and (i-1 in S):
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + 1
        if (n+i in S) and (n+i-1 in S):
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + 1
        if (i in S) and (n+i in S):
            dp[i][3] = max(dp[i-1]) + 1

    return max(dp[r-1])

def startpos(A):
    flag = False
    for i in range(n):
        if flag == True and i in A:
            return i
        elif flag == False and i not in A:
            flag = True
    return 0

def matching(L,cycle):
    A = set(map(lambda x:x%n, L))
    B = set(L)
    #cycle = len(A) == n
    res = 0
    start = 0

    if cycle:
        res = max(fillblocks(B,n,0),res)

        if (0 in B) and (n-1 in B):
            B.remove(0)
            B.remove(n-1)
            res = max(fillblocks(B,n,1),res)
            B.add(0)
            B.add(n-1)

        if (n in B) and (2*n-1 in B):
            B.remove(n)
            B.remove(2*n-1)
            res = max(fillblocks(B,n,2),res)
            B.add(n)
            B.add(2*n-1)
    else:
        #decide starting point
        start = startpos(A)

        #shift the set
        C = set()
        for i in B:
            if i < n:
                C.add((i+n-start)%n)
            else:
                C.add(n+(i+n-start)%n)

        res = fillblocks(C,len(A),0)

    return res

for _ in range(T):
    n,w = map(int,input().split())
    L = list(map(int,input().split())) + list(map(int,input().split()))

    if n == 1:
        print(2-(L[0]+L[1] <= w))
        continue

    Mergeable = []
    for i in range(n):
        merge(i,(i+1)%n)
        merge(i,i+n)
        merge(i+n,(i+1)%n+n)

    N = [Node(i) for i in range(2*n)]
    cycle = False
    for i in Mergeable:
        a,b = i
        N[a].union(N[b])

    S = set()
    for i in N:
        S.add(tuple(i.find().group))

    ans = 2*n
    for i in S:
        if len(i) >= 2:
            ans -= matching(i,False)

    print(ans)