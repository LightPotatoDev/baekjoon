import sys
input = sys.stdin.readline

def treeInit(start,end,node):
    val = min(L[start:end+1])
    Tree[node] = val
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def check(left,right):
    nodeNum = [[1,n,1]]
    checking = []
    mini = int(1e12)
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
        mini = min(mini,Tree[i])
    return mini

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
            Tree[p] = val
            continue
        Tree[p] = min(Tree[p*2], Tree[p*2+1])

n = int(input())
L = [0] + list(map(int,input().split()))
q = int(input())
Tree = [0]*(n*4)
treeInit(1,n,1)

for _ in range(q):
    a,b,c = map(int,input().split())
    if a == 1:
        change(b,c)
    if a == 2:
        print(check(b,c))
