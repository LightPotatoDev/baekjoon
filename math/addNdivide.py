import sys
from collections import deque

sys.setrecursionlimit(10**5)
n = int(input())
L = deque([i for i in range(2,1000001)])

def checksum(A,s):
    times = 0
    for i in A:
        if s % i == 0:
            times += 1
        if times >= 2:
            return False
    return times == 1

def picknumber(index,subset,total):
    if index >= n:
        if checksum(subset,total):
            print(*subset)
            exit(0)
        return

    for i in range(len(L)):
        p = L.popleft()
        picknumber(index+1,subset+[p],total+p)

picknumber(0,[],0)