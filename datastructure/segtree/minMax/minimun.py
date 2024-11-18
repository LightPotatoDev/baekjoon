import sys
input = sys.stdin.readline

def treeInit(start,end,node):
    val = min(L[start:end+1])
    Tree[node] = val
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def check(left,right):
    nodeNum = [[1,n,1]]
    checking = []
    mini = int(1e12)
    while nodeNum:
        start,end,node = nodeNum.pop()
        if (left <= start and end <= right):
            checking.append(node)
            continue
        if (left <= end and right >= start):
            mid = (start+end) // 2
            nodeNum.append([start,mid,node*2])
            nodeNum.append([mid+1,end,node*2+1])

    for i in checking:
        mini = min(mini,Tree[i])
    return mini

n,m = map(int,input().split())
L = [0] + [int(input()) for _ in range(n)]
S = L[:]
for i in range(n):
    S[i+1] += S[i]
Tree = [0]*(n*4)
treeInit(1,n,1)

for _ in range(m):
    l,r = map(int,input().split())
    print(check(l,r))