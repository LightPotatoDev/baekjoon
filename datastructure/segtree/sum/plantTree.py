import sys
input = sys.stdin.readline

def treeInit(start,end,node):
    Tree[node] = A[end]-A[start-1]
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def getSum(left,right):
    nodeNum = [[1,n,1]]
    s = 0
    while nodeNum:
        start,end,node = nodeNum.pop()
        if (left <= start and end <= right):
            s += Tree[node]
            continue
        if (left <= end and right >= start):
            mid = (start+end) // 2
            nodeNum.append([start,mid,node*2])
            nodeNum.append([mid+1,end,node*2+1])

    return s

n = int(input())
A = [0]+[int(input()) for _ in range(n)]
L = [0]*(n+1)
Tree = [0]*(n*4)
for i in range(1,n+1):
    L[i] = abs(A[i]-A[i-1])
treeInit(1,n,1)
print(L)
res = 0
ans = 1
mod = int(1e9)+7
for i in range(n+1,1,-1):
    res += getSum(i,n+1)
    ans = ans * res % mod
    print(res,ans)
print(ans)