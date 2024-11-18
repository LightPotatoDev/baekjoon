import sys
import math
input = sys.stdin.readline

n = int(input())
size = int(2e6)
Tree = [0]*(2**((math.ceil(math.log(size,2)))+1))

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

def getCandy(start,end,node,rank,cur):
    if (start == end):
        return start

    mid = (start + end) // 2
    if (Tree[node*2] >= rank-cur):
        return getCandy(start,mid,node*2,rank,cur)
    else:
        return getCandy(mid+1,end,node*2+1,rank,cur+Tree[node*2])

for _ in range(n):
    a,b = map(int,input().split())
    if a == 1:
        change(1,size,1,b,1)
    if a == 2:
        c = getCandy(1,size,1,b,0)
        print(c)
        change(1,size,1,c,-1)