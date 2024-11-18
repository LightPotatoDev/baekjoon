import sys
input = sys.stdin.readline

def change(pos,val):
    start,end,node = 1,d,1
    nodeNum = []
    while True:
        nodeNum.append([node,start,end])
        if start == end:
            break
        mid = (start + end) // 2
        if start <= pos <= mid:
            end = mid
            node *= 2
        else:
            start = mid+1
            node = node*2+1

    while nodeNum:
        p,s,e = nodeNum.pop()
        if (s == e):
            Tree[p] = val
            continue
        Tree[p] = max(Tree[p*2], Tree[p*2+1])

n,d = map(int,input().split())
L = list(map(int,input().split()))
Tree = [0]*(d*4)
ans = 0

for i in range(n):
    val = Tree[1] + L[i]
    ans = max(ans,val)
    change(i%d+1,max(0,val))

if ans != 0:
    print(ans)
else:
    print(max(L))