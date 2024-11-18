import sys
input = sys.stdin.readline

n = int(input())
size = int(1e6)
Tree = [0]*(size*4)

def change(start,end,node,pos,add):
    if not (start <= pos <= end):
        return
    Tree[node] += add
    if (start == end):
        return

    mid = (start + end) // 2
    change(start,mid,node*2,pos,add)
    change(mid+1,end,node*2+1,pos,add)

def getCandy(start,end,node,rank,cur):
    if (start == end):
        return start

    mid = (start + end) // 2
    if (Tree[node*2] >= rank-cur):
        return getCandy(start,mid,node*2,rank,cur)
    else:
        return getCandy(mid+1,end,node*2+1,rank,cur+Tree[node*2])

for _ in range(n):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        a,b = cmd
        c = getCandy(1,size,1,b,0)
        print(c)
        change(1,size,1,c,-1)
    if cmd[0] == 2:
        a,b,c = cmd
        change(1,size,1,b,c)