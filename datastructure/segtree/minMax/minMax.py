import sys
input = sys.stdin.readline

n,m = map(int,input().split())
L = [0]+[int(input()) for _ in range(n)]
Tree = [0]*(n*4)

def treeInit(start,end,node):
    Tree[node] = [min(L[start:end+1]),max(L[start:end+1])]
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def partialMin(start,end,node,left,right):
    if (left > end or right < start):
        return int(1e9)+1
    if (left <= start and end <= right):
        return Tree[node][0]

    mid = (start + end) // 2
    return min(partialMin(start,mid,node*2,left,right), partialMin(mid+1,end,node*2+1,left,right))

def partialMax(start,end,node,left,right):
    if (left > end or right < start):
        return 0
    if (left <= start and end <= right):
        return Tree[node][1]

    mid = (start + end) // 2
    return max(partialMax(start,mid,node*2,left,right), partialMax(mid+1,end,node*2+1,left,right))

treeInit(1,n,1)
for _ in range(m):
    a,b = map(int,input().split())
    print(partialMin(1,n,1,a,b), partialMax(1,n,1,a,b))
