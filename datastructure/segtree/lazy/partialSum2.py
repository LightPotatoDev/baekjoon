import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.odd = 0
        self.even = 0

    def __repr__(self):
        return f"{self.odd} {self.even}"

def treeInit(start,end,node):
    Tree[node].odd  = L[start:end+1].count(1)
    Tree[node].even = L[start:end+1].count(0)

    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def change(pos,prev,now):
    if (prev == now):
        return

    start,end,node = 1,n,1
    while True:
        if  prev == 0: Tree[node].even -= 1
        elif prev == 1: Tree[node].odd -= 1

        if  now == 0: Tree[node].even += 1
        elif now == 1: Tree[node].odd += 1

        if start == end:
            return
        mid = (start + end) // 2
        if start <= pos <= mid:
            end = mid
            node *= 2
        else:
            start = mid+1
            node = node*2+1

def getOdd(cmd,left,right):
    nodeNum = [[1,n,1]]
    odd,even = 0,0
    while nodeNum:
        start,end,node = nodeNum.pop()
        if (left <= start and end <= right):
            odd += Tree[node].odd
            even += Tree[node].even
            continue
        if (left <= end and right >= start):
            mid = (start+end) // 2
            nodeNum.append([start,mid,node*2])
            nodeNum.append([mid+1,end,node*2+1])

    if cmd == 2:
        return even
    else:
        return odd

n = int(input())
Tree = [Node() for _ in range(n*4)]
L = [0]+list(map(lambda x: int(x)%2,input().split()))
treeInit(1,n,1)

k = int(input())
for _ in range(k):
    a,b,c = map(int,input().split())
    if a == 1:
        change(b,L[b],c%2)
        L[b] = c%2
    else:
        print(getOdd(a,b,c))
