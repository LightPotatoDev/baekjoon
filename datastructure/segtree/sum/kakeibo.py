import sys
input = sys.stdin.readline

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



for _ in range(q):
    a,b,c = map(int,input().split())
    if a == 1:
        change(1,n,1,b,c)
    if a == 2:
        print(getSum(1,n,1,b,c))