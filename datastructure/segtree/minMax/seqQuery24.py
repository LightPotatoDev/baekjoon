import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.max = 0
        self.ind = 0

    def __repr__(self):
        return f"{self.max} {self.ind}"

def treeInit(start,end,node):
    val = max(L[start:end+1])
    Tree[node].ind = L[start:end+1].index(val)+start
    Tree[node].max = val
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def check(left,right):
    nodeNum = [[1,n,1]]
    checking = []
    maxi = [0,0]
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
        maxi = max(maxi,[Tree[i].max,Tree[i].ind])
    return maxi


def change(pos,val):
    start,end,node = 1,n,1
    nodeNum = []
    while True:
        nodeNum.append([node,start,end])
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
        p,s,e = nodeNum.pop()
        if (s == e):
            Tree[p].max = val
            Tree[p].ind = pos
            continue
        Tree[p].max,Tree[p].ind = max([Tree[p*2].max,Tree[p*2].ind], [Tree[p*2+1].max,Tree[p*2+1].ind])

n = int(input())
Tree = [Node() for i in range(1,n*4+1)]
L = [0]+list(map(int,input().split()))
treeInit(1,n,1)

k = int(input())
for _ in range(k):
    q,a,b = map(int,input().split())
    if q == 1:
        change(a,b)
        L[a] = b
    if q == 2:
        ai, idx = check(a,b)
        change(idx,0)
        aj, idx2 = check(a,b)
        change(idx,ai)
        print(ai+aj)