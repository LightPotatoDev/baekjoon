import sys
input = sys.stdin.readline

n,k = map(int,input().split())
L = [int(input()) for _ in range(n)]
SIZE = 65536+1

Tree = [0]*(SIZE*4)

def change(pos,add):
    start,end,node = 1,SIZE,1
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

def getSum(left,right):
    nodeNum = [[1,SIZE,1]]
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

def medianSearch():
    lo = 0
    hi = SIZE

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if getSum(1,mid) < (k+1)//2:
            lo = mid
        else:
            hi = mid
    return hi

ans = 0
for i in range(n):
    change(L[i]+1,1)
    if (i >= k):
        change(L[i-k]+1, -1)
    if (i >= k-1):
        ans += medianSearch()

print(ans-(n-k+1))
