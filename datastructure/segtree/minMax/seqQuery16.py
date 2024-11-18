import sys
input = sys.stdin.readline

n = int(input())
L = [0]+list(map(int,input().split()))
Tree = [0]*(n*4)

def treeInit(start,end,node):
    val = min(L[start:end+1])
    Tree[node] = [val,L[start:end+1].index(val)+start]
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def change(start,end,node,pos,val):
    if not (start <= pos <= end):
        return Tree[node]
    if (start == end):
        Tree[node] = [val,pos]
        return Tree[node]

    mid = (start + end) // 2
    v1 = change(start,mid,node*2,pos,val)
    v2 = change(mid+1,end,node*2+1,pos,val)
    Tree[node] = min(v1,v2,key=lambda x:(x[0],x[1]))
    return Tree[node]

def partialMin(start,end,node,left,right):
    if (left > end or right < start):
        return [int(1e9)+1,-1]
    if (left <= start and end <= right):
        return Tree[node]

    mid = (start + end) // 2
    v1 = partialMin(start,mid,node*2,left,right)
    v2 = partialMin(mid+1,end,node*2+1,left,right)
    return min(v1,v2,key = lambda x:(x[0],x[1]))

treeInit(1,n,1)
m = int(input())
for _ in range(m):
    c,a,b = map(int,input().split())
    #print(Tree)
    if c == 1:
        change(1,n,1,a,b)
    if c == 2:
        print(partialMin(1,n,1,a,b)[1])
