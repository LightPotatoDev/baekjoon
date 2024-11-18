import sys
input = sys.stdin.readline

n,k = map(int,input().split())
Tree = [0]*(n+2)

def treeInit():
    for i in range(1,n+1):
        p = 0
        while (i >> p) & 1 == 0:
            p += 1
        Tree[i] = 2**p

def change(idx,add):
    while (idx <= n):
        Tree[idx] += add
        idx += idx & -idx

def getSum(idx):
    s = 0
    while idx > 0:
        s += Tree[idx]
        idx &= (idx - 1)
    return s

def binSearch(l,target):
    lo = -1
    hi = n+1
    sum = 0
    lSum = getSum(l)

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        sum = getSum(mid) - lSum

        if sum < target:
            lo = mid
        else:
            hi = mid

    if sum+1 >= target and hi <= n:
        return [hi,1]
    else:
        return [sum,0]

start = 0
ans = []
treeInit()
for i in range(n):
    target = k
    res, ok = binSearch(start,target)

    if ok == 0:
        target -= res
        target = (target-1) % min(n-i,k) + 1
        start  = 0
        res, ok = binSearch(start,target)

    change(res,-1)
    ans.append(res)
    start = res

print("<"+', '.join(map(str,ans))+">")
