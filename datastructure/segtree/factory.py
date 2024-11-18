import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
D = dict()
for i,x in enumerate(A):
    D[x] = i+1
for i,x in enumerate(B):
    B[i] = D[x]

Tree = [0]*(n*4)

def change(start,end,node,pos,add):
    if not (start <= pos <= end):
        return
    Tree[node] += add
    if (start == end):
        return

    mid = (start + end) // 2
    change(start,mid,node*2,pos,add)
    change(mid+1,end,node*2+1,pos,add)

def getSum(start,end,node,left,right):
    if (left > end or right < start):
        return 0
    if (left <= start and end <= right):
        return Tree[node]

    mid = (start + end) // 2
    return getSum(start,mid,node*2,left,right) + getSum(mid+1,end,node*2+1,left,right)

ans = 0
for i in B:
    ans += getSum(1,n,1,i,n)
    change(1,n,1,i,1)

print(ans)