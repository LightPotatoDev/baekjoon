import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.plus = 0
        self.minus = 0
        self.zeros = 0

    def __repr__(self):
        return f"{self.plus} {self.minus} {self.zeros}"

def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    return 0

def treeInit(start,end,node):
    Tree[node].plus  = L[start:end+1].count(1)
    Tree[node].minus = L[start:end+1].count(-1)
    Tree[node].zeros = L[start:end+1].count(0)
    if start == end:
        return
    mid = (start + end) // 2
    treeInit(start, mid, node*2)
    treeInit(mid+1, end, node*2+1)

def change(pos,prev,now):
    if (prev == now):
        return

    start,end,node = 1,n,1
    while True:
        if  prev == -1: Tree[node].minus -= 1
        elif prev == 1: Tree[node].plus -= 1
        elif prev == 0: Tree[node].zeros -= 1

        if  now == -1: Tree[node].minus += 1
        elif now == 1: Tree[node].plus += 1
        elif now == 0: Tree[node].zeros += 1

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
    plus,minus,zeros = 0,0,0
    while nodeNum:
        start,end,node = nodeNum.pop()
        if (left <= start and end <= right):
            plus += Tree[node].plus
            minus += Tree[node].minus
            zeros += Tree[node].zeros
            continue
        if (left <= end and right >= start):
            mid = (start+end) // 2
            nodeNum.append([start,mid,node*2])
            nodeNum.append([mid+1,end,node*2+1])

    if (zeros > 0):
        return "0"
    elif minus % 2 == 0:
        return "+"
    else:
        return "-"

while True:
    n,k = 0,0
    try:
        n,k = map(int,input().split())
    except:
        break

    Tree = [Node() for _ in range(n*4)]
    L = [0]+list(map(lambda x: sign(int(x)),input().split()))
    treeInit(1,n,1)

    for _ in range(k):
        cmd = list(input().rstrip().split())
        if cmd[0] == "C":
            ind,num = map(int,cmd[1:])
            num = sign(num)
            change(ind,L[ind],num)
            L[ind] = num
        if cmd[0] == "P":
            l,r = map(int,cmd[1:])
            print(getMul(l,r),end='')
    print('')