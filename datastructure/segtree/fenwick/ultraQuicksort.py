import sys
input = sys.stdin.readline
from bisect import bisect_right

def change(pos,add):
    start,end,node = 1,n,1
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
    nodeNum = [[1,n,1]]
    checking = []
    s = 0
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
        s += Tree[i]
    return s

while True:
    n = int(input())

    if n == 0:
        break

    A = [int(input()) for _ in range(n)]
    B = sorted(A)

    Tree = [0]*(n*4)

    ans = 0

    for run in A:
        i = bisect_right(B,run)
        ans += getSum(i+1,n)
        change(i,1)

    print(ans)