import sys
input = sys.stdin.readline

mod = int(1e9)+7
n,m,k = map(int,input().split())
L = [0]+[int(input()) for _ in range(n)]
Zero = [0]*(n*4)
Tree = [0]*(n*4)

def multiply(start,end):
    s = 1
    for i in range(start,end+1):
        s = (s * L[i]) % mod
    return s

def treeInit(start,end,node):
    Tree[node] = multiply(start,end)
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def change(pos,prev,now):
    start,end,node = 1,n,1
    setZero = now==0
    if(now == 0):
        now = 1
    while True:
        Zero[node] = setZero
        Tree[node] = (Tree[node] * pow(prev,-1,mod)) % mod
        Tree[node] = (Tree[node] * now) % mod
        if start == end:
            return
        mid = (start + end) // 2
        if start <= pos <= mid:
            end = mid
            node *= 2
        else:
            start = mid+1
            node = node*2+1

def getMul(left,right):
    nodeNum = [[1,n,1]]
    s = 1
    while nodeNum:
        start,end,node = nodeNum.pop()
        if (left <= start and end <= right):
            s *= Tree[node]
            s %= mod
            if (Zero[node] == 1):
                s = 0
                break
            continue
        if (left <= end and right >= start):
            mid = (start+end) // 2
            nodeNum.append([start,mid,node*2])
            nodeNum.append([mid+1,end,node*2+1])

    return s

treeInit(1,n,1)
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if (a == 1):
        change(b,L[b],c)
        L[b] = c
        if (c == 0):
            L[b] = 1
    if (a == 2):
        print(getMul(b,c))