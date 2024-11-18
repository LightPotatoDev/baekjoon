import sys
input = sys.stdin.readline

class Node:
    def __init__(self,data):
        self.data = data
        self.min = 0
        self.max = 0

    def __repr__(self):
        return f"{self.min} {self.max}"

def treeInit(start,end,node):
    Tree[node].min = start
    Tree[node].max = end
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def check(left,right):
    nodeNum = [[0,n-1,1]]
    checking = []
    mini = int(1e12)
    maxi = 0
    while nodeNum:
        start,end,node = nodeNum.pop()
        if (left <= start and end <= right):
            checking.append(node)
            continue
        if (left <= end and right >= start):
            mid = (start+end) // 2
            nodeNum.append([start,mid,node*2])
            nodeNum.append([mid+1,end,node*2+1])

    for i in checking:
        mini = min(mini,Tree[i].min)
        maxi = max(maxi,Tree[i].max)
    return left == mini and right == maxi


def change(start,end,node,pos,val):
    nodeNum = []
    while True:
        nodeNum.append(node)
        if start == end:
            break
        mid = (start + end) // 2
        if start <= pos <= mid:
            end = mid
            node *= 2
        else:
            start = mid+1
            node = node*2+1

    while nodeNum:
        p = nodeNum.pop()
        if Tree[p].min == Tree[p].max:
            Tree[p].min = val
            Tree[p].max = val
            continue

        Tree[p].min = min(Tree[p*2].min, Tree[p*2+1].min)
        Tree[p].max = max(Tree[p*2].max, Tree[p*2+1].max)

T = int(input())

for _ in range(T):
    n,k = map(int,input().split())
    Tree = [Node(i) for i in range(1,n*4+1)]
    L = [i for i in range(n)]
    treeInit(0,n-1,1)

    for _ in range(k):
        q,a,b = map(int,input().split())
        if q == 0:
            change(0,n-1,1,a,L[b])
            change(0,n-1,1,b,L[a])
            L[a],L[b] = L[b],L[a]
        if q == 1:
            if check(a,b):
                print("YES")
            else:
                print("NO")