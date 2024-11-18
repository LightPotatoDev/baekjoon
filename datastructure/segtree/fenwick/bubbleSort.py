import sys
input = sys.stdin.readline
from bisect import bisect_left


n = int(input())
A = list(map(int,input().split()))
D = {}
for i,x in enumerate(sorted(set(A))):
    D[x] = i+1
L = []
for i in A:
    L.append(D[i])

Tree = [0]*(n*4)

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

ans = 0
for i in L:
    ans += getSum(1,n,1,i+1,n)
    change(1,n,1,i,1)

print(ans)