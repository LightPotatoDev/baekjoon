import sys
input = sys.stdin.readline

mod = int(1e9)+7
n,m,k = map(int,input().split())
L = [0]+[int(input()) for _ in range(n)]
Tree = [0]*(n*4)

def mul(start,end):
    s = 1
    for i in range(start,end+1):
        s = (s * L[i]) % mod
    return s

def treeInit(start,end,node):
    Tree[node] = mul(start,end)
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def change(start,end,node,pos):
    if not (start <= pos <= end):
        return
    Tree[node] = mul(start,end)
    if (start == end):
        return

    mid = (start + end) // 2
    change(start,mid,node*2,pos)
    change(mid+1,end,node*2+1,pos)

def getMul(start,end,node,left,right):
    if (left > end or right < start):
        return 1
    if (left <= start and end <= right):
        return Tree[node]

    mid = (start + end) // 2
    return (getMul(start,mid,node*2,left,right) * getMul(mid+1,end,node*2+1,left,right)) % mod

treeInit(1,n,1)
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if (a == 1):
        L[b] = c
        change(1,n,1,b)
    if (a == 2):
        print(getMul(1,n,1,b,c))