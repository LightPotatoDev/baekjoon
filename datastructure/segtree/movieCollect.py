import sys
input = sys.stdin.readline

T = int(input())

def treeInit(start,end,node):
    Tree[node] = S[end]-S[start-1]
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def change(start,end,node,pos,add):
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

def getSum(start,end,node,left,right):
    if (left > end or right < start):
        return 0
    if (left <= start and end <= right):
        return Tree[node]

    mid = (start + end) // 2
    return getSum(start,mid,node*2,left,right) + getSum(mid+1,end,node*2+1,left,right)

for _ in range(T):
    n,m = map(int,input().split())
    L = list(map(int,input().split()))
    Ind = [i+m+1 for i in range(n)]
    Tree = [0] * ((n+m)*4)
    S = [0]*(n+m+1)
    Ans = []

    for i in range(n):
        S[i+m+1] = i+1
    treeInit(1,n+m,1)

    for i in range(m):
        dvdPos = Ind[L[i]-1]
        Ans.append(getSum(1,n+m,1,1,dvdPos-1))
        Ind[L[i]-1] = m-i
        change(1,n+m,1,dvdPos,-1)
        change(1,n+m,1,m-i,1)

    print(*Ans)