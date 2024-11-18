import sys
input = sys.stdin.readline

def treeInit(start,end,node):
    Tree[node] = S[end]-S[start-1]
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def getSum(start,end,node,left,right):
    if (left > end or right < start):
        return 0
    if (left <= start and end <= right):
        return Tree[node]

    mid = (start + end) // 2
    return getSum(start,mid,node*2,left,right) + getSum(mid+1,end,node*2+1,left,right)

def change(pos,add):
    start,end,node = 1,n,1
    while True:
        Tree[node] += add
        if start == end:
            return
        mid = (start + end) // 2
        if start <= pos <= mid:
            end = mid
            node *= 2
        else:
            start = mid+1
            node = node*2+1

n = int(input())
Tree = [0]*(n*4)
A = [0]+list(map(int,input().split()))
B = [0]+[A[i+1]-A[i] for i in range(n)]

S = B[:]
for i in range(n):
    S[i+1] += S[i]
treeInit(1,n,1)

m = int(input())
for _ in range(m):
    query = list(map(int,input().split()))
    if query[0] == 1:
        q,i,j,k = query
        change(i,k)
        if (j+1 <= n):
            change(j+1,-k)
    if query[0] == 2:
        print(getSum(1,n,1,1,query[1]))